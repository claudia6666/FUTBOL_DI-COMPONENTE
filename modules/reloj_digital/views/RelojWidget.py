
from PySide6.QtWidgets import QWidget, QMessageBox, QLCDNumber, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QTimer, QTime, Signal, Property, Qt, QFile, QCoreApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPalette, QColor
from enum import Enum
import os


class ClockMode(Enum):
    CLOCK = "clock"
    TIMER = "timer"


class DigitalClockWidget(QWidget):
    
    alarmTriggered = Signal(str)
    timerFinished = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self._mode = ClockMode.CLOCK
        self._format_24h = True
        self._alarm_enabled = False
        self._alarm_hour = 0
        self._alarm_minute = 0
        self._alarm_message = "Alarm!"
        self._alarm_triggered_today = False
        
        self._timer_duration = 90
        self._timer_running = False
        self._timer_paused = False
        self._elapsed_seconds = 0
        self._count_up = True
        
        self.lcd_display = None
        self.btn_start = None
        self.btn_pause = None
        self.btn_reset = None
        self.controls_layout = None
        
        self._setup_ui()
        
        self._update_timer = QTimer(self)
        self._update_timer.timeout.connect(self._update_display)
        self._update_timer.start(1000)
        
    def _setup_ui(self):
        ui_file_path = os.path.join(os.path.dirname(__file__), "..", "ui", "RelojWidget.ui")
        ui_file = QFile(ui_file_path)
        if not ui_file.open(QFile.ReadOnly):
            print(f"Error: No se puede abrir el archivo {ui_file_path}")
            self._setup_ui_fallback()
            return
        loader = QUiLoader()
        ui_widget = loader.load(ui_file, self)
        ui_file.close()

        if ui_widget is None:
            print("Error: No se pudo cargar la interfaz")
            self._setup_ui_fallback()
            return

        self.lcd_display = ui_widget.findChild(QLCDNumber, "lcdDisplay")
        self.btn_start = ui_widget.findChild(QPushButton, "btnStart")
        self.btn_pause = ui_widget.findChild(QPushButton, "btnPause")
        self.btn_reset = ui_widget.findChild(QPushButton, "btnReset")

        if self.btn_start:
            self.btn_start.clicked.connect(self.start_timer)
        if self.btn_pause:
            self.btn_pause.clicked.connect(self.pause_timer)
        if self.btn_reset:
            self.btn_reset.clicked.connect(self.reset_timer)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(ui_widget)

        self._update_controls_visibility()
        
    def _setup_ui_fallback(self):
        from PySide6.QtWidgets import QLCDNumber
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(2, 2, 2, 2)
        
        self.lcd_display = QLCDNumber(self)
        self.lcd_display.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_display.setDigitCount(8)
        self.lcd_display.setMinimumHeight(60)
        
        layout.addWidget(self.lcd_display)
        
        self.controls_layout = QHBoxLayout()
        self.controls_layout.setSpacing(1)
        self.controls_layout.setContentsMargins(0, 1, 0, 1)
        
        self.btn_start = QPushButton(self)
        self.btn_start.clicked.connect(self.start_timer)
        self.btn_start.setMinimumHeight(14)
        self.btn_start.setMaximumHeight(14)
        
        self.btn_pause = QPushButton(self)
        self.btn_pause.clicked.connect(self.pause_timer)
        self.btn_pause.setEnabled(False)
        self.btn_pause.setMinimumHeight(14)
        self.btn_pause.setMaximumHeight(14)
        
        self.btn_reset = QPushButton(self)
        self.btn_reset.clicked.connect(self.reset_timer)
        self.btn_reset.setMinimumHeight(14)
        self.btn_reset.setMaximumHeight(14)
        
        self.controls_layout.addWidget(self.btn_start)
        self.controls_layout.addWidget(self.btn_pause)
        self.controls_layout.addWidget(self.btn_reset)
        
        layout.addLayout(self.controls_layout)
        
        self.retranslateUi()
        self._update_controls_visibility()
        
    def _update_display(self):
        if self._mode == ClockMode.CLOCK:
            self._update_clock_display()
        else:
            self._update_timer_display()
            
    def _update_clock_display(self):
        current_time = QTime.currentTime()
        
        if self._format_24h:
            time_text = current_time.toString("hh:mm:ss")
        else:
            hour = current_time.hour()
            minute = current_time.minute()
            second = current_time.second()
            
            ampm = "AM" if hour < 12 else "PM"
            hour_12 = hour % 12
            if hour_12 == 0:
                hour_12 = 12
            
            time_text = f"{hour_12:02d}:{minute:02d}:{second:02d} {ampm}"
            
        self.lcd_display.display(time_text)
        
        if self._alarm_enabled and not self._alarm_triggered_today:
            if (current_time.hour() == self._alarm_hour and 
                current_time.minute() == self._alarm_minute and
                current_time.second() == 0):
                self._trigger_alarm()
                
    def _update_timer_display(self):
        if self._timer_running and not self._timer_paused:
            if self._count_up:
                self._elapsed_seconds += 1
                total_seconds = self._elapsed_seconds
            else:
                total_seconds = (self._timer_duration * 60) - self._elapsed_seconds
                self._elapsed_seconds += 1

                if total_seconds <= 0:
                    total_seconds = 0
                    self._timer_running = False
                    self.timerFinished.emit()
                    self.btn_start.setEnabled(True)
                    self.btn_pause.setEnabled(False)
        else:
            if self._count_up:
                total_seconds = self._elapsed_seconds
            else:
                total_seconds = (self._timer_duration * 60) - self._elapsed_seconds
                if total_seconds < 0:
                    total_seconds = 0
        
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        time_text = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.lcd_display.display(time_text)
        
    def _trigger_alarm(self):
        self._alarm_triggered_today = True
        self.alarmTriggered.emit(self._alarm_message)
        
        QMessageBox.information(self, self.tr("Alarm"), self._alarm_message)
        
    def _update_controls_visibility(self):
        visible = (self._mode == ClockMode.TIMER)
        self.btn_start.setVisible(visible)
        self.btn_pause.setVisible(visible)
        self.btn_reset.setVisible(visible)
        
    def start_timer(self):
        self._timer_running = True
        self._timer_paused = False
        self.btn_start.setEnabled(False)
        self.btn_pause.setEnabled(True)
        
    def pause_timer(self):
        self._timer_paused = True
        self.btn_start.setEnabled(True)
        self.btn_pause.setEnabled(False)
        
    def reset_timer(self):
        self._timer_running = False
        self._timer_paused = False
        self._elapsed_seconds = 0
        self.btn_start.setEnabled(True)
        self.btn_pause.setEnabled(False)
        self._update_display()
        
    def get_elapsed_time(self):
        return self._elapsed_seconds
    
    def get_remaining_time(self):
        if self._count_up:
            return 0
        return max(0, (self._timer_duration * 60) - self._elapsed_seconds)
        
    def get_mode(self):
        return self._mode
        
    def set_mode(self, mode):
        if isinstance(mode, str):
            try:
                mode = ClockMode(mode)
            except ValueError:
                print(f"Modo inválido: {mode}. Usando CLOCK por defecto.")
                mode = ClockMode.CLOCK
        
        if not isinstance(mode, ClockMode):
            print(f"Tipo de modo inválido. Usando CLOCK por defecto.")
            mode = ClockMode.CLOCK
            
        self._mode = mode
        self._update_controls_visibility()
        self._update_display()
        
    mode = Property(str, lambda self: self.get_mode().value, set_mode)
    
    def get_format_24h(self):
        return self._format_24h
        
    def set_format_24h(self, value):
        self._format_24h = bool(value)
        if self.lcd_display:
            if self._format_24h:
                self.lcd_display.setDigitCount(8)  # HH:MM:SS
            else:
                self.lcd_display.setDigitCount(11)  # HH:MM:SS AM
        self._update_display()
        
    format24h = Property(bool, get_format_24h, set_format_24h)
    
    def get_alarm_enabled(self):
        return self._alarm_enabled
        
    def set_alarm_enabled(self, value):
        self._alarm_enabled = bool(value)
        if not self._alarm_enabled:
            self._alarm_triggered_today = False
        
    alarmEnabled = Property(bool, get_alarm_enabled, set_alarm_enabled)
    
    def get_alarm_hour(self):
        return self._alarm_hour
        
    def set_alarm_hour(self, value):
        try:
            hour = int(value)
            self._alarm_hour = max(0, min(23, hour))
            self._alarm_triggered_today = False
        except (ValueError, TypeError):
            print(f"Valor de hora inválido: {value}")
        
    alarmHour = Property(int, get_alarm_hour, set_alarm_hour)
    
    def get_alarm_minute(self):
        return self._alarm_minute
        
    def set_alarm_minute(self, value):
        try:
            minute = int(value)
            self._alarm_minute = max(0, min(59, minute))
            self._alarm_triggered_today = False
        except (ValueError, TypeError):
            print(f"Valor de minuto inválido: {value}")
        
    alarmMinute = Property(int, get_alarm_minute, set_alarm_minute)
    
    def get_alarm_message(self):
        return self._alarm_message
        
    def set_alarm_message(self, value):
        self._alarm_message = str(value) if value else "Alarm!"
        
    alarmMessage = Property(str, get_alarm_message, set_alarm_message)
    
    def get_timer_duration(self):
        return self._timer_duration
        
    def set_timer_duration(self, value):
        try:
            duration = int(value)
            self._timer_duration = max(1, duration)
            if self._elapsed_seconds > (self._timer_duration * 60):
                self._elapsed_seconds = 0
        except (ValueError, TypeError):
            print(f"Valor de duración inválido: {value}")
        
    timerDuration = Property(int, get_timer_duration, set_timer_duration)
    
    def get_count_up(self):
        return self._count_up
        
    def set_count_up(self, value):
        self._count_up = bool(value)
        self._update_display()
        
    countUp = Property(bool, get_count_up, set_count_up)
    

    def changeEvent(self, event):
        if event.type() == event.Type.LanguageChange:
            self.retranslateUi()
        super().changeEvent(event)
        
    def retranslateUi(self):
        if self.btn_start:
            self.btn_start.setText(QCoreApplication.translate("DigitalClockWidget", "Start"))
        if self.btn_pause:
            self.btn_pause.setText(QCoreApplication.translate("DigitalClockWidget", "Pause"))
        if self.btn_reset:
            self.btn_reset.setText(QCoreApplication.translate("DigitalClockWidget", "Reset"))