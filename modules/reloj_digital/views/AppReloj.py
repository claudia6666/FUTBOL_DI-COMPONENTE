import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PySide6.QtCore import QTranslator, QCoreApplication
from ..widgets.ui_AppReloj import Ui_MainWindow
from .RelojWidget import DigitalClockWidget
from models.globals import get_db_connection


class TestWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.translator = QTranslator()
        self.qt_translator = QTranslator()
        self.clock_widget = None
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        if self.ui.clockWidgetContainer:
            container_layout = QVBoxLayout(self.ui.clockWidgetContainer)
            container_layout.setContentsMargins(0, 0, 0, 0)
            
            self.clock_widget = DigitalClockWidget()
            container_layout.addWidget(self.clock_widget)
            self.clock_widget.alarmTriggered.connect(self.on_alarm_triggered)
            self.clock_widget.timerFinished.connect(self.on_timer_finished)
        
        if self.ui.comboLanguage:
            self.ui.comboLanguage.currentIndexChanged.connect(self.change_language)
        if self.ui.radioClock:
            self.ui.radioClock.toggled.connect(self.on_mode_changed)
        if self.ui.check24h:
            self.ui.check24h.toggled.connect(lambda c: self.clock_widget.set_format_24h(c))
        if self.ui.checkAlarm:
            self.ui.checkAlarm.toggled.connect(lambda c: self.clock_widget.set_alarm_enabled(c))
        if self.ui.spinAlarmHour:
            self.ui.spinAlarmHour.valueChanged.connect(lambda v: self.clock_widget.set_alarm_hour(v))
        if self.ui.spinAlarmMinute:
            self.ui.spinAlarmMinute.valueChanged.connect(lambda v: self.clock_widget.set_alarm_minute(v))
        if self.ui.editAlarmMessage:
            self.ui.editAlarmMessage.textChanged.connect(lambda t: self.clock_widget.set_alarm_message(t))
        if self.ui.spinTimerDuration:
            self.ui.spinTimerDuration.valueChanged.connect(lambda v: self.clock_widget.set_timer_duration(v))
        if self.ui.checkCountUp:
            self.ui.checkCountUp.toggled.connect(lambda c: self.clock_widget.set_count_up(c))
        self.change_language(0)
    
    def on_mode_changed(self, checked):
        if checked:
            self.clock_widget.set_mode("clock")
        else:
            self.clock_widget.set_mode("timer")
    
    def on_alarm_triggered(self, message):
        self.ui.labelEvents.setText(message)
        self.ui.labelEvents.setStyleSheet(
            "background-color: #ffffff; padding: 10px; border: 1px solid #cccccc; "
            "border-radius: 5px; font-weight: normal; color: #000000;"
        )
    
    def on_timer_finished(self):
        msg = QCoreApplication.translate("TestWindow", "TIMER FINISHED!")
        self.ui.labelEvents.setText(f" {msg}")
        self.ui.labelEvents.setStyleSheet(
            "background-color: #ffffff; padding: 10px; border: 1px solid #cccccc; "
            "border-radius: 5px; font-weight: normal; color: #000000;"
        )
    
    def change_language(self, index):
        languages = {0: "es", 1: "en"}
        lang_code = languages.get(index)
        if not lang_code:
            return
        
        app = QApplication.instance()
        
        translator_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "translations",
            f"clock_{lang_code}.qm"
        )
        
        app.removeTranslator(self.translator)

        
        if os.path.exists(translator_path):
            if self.translator.load(translator_path):
                app.installTranslator(self.translator)
                print(f"✓ Idioma cambiado a: {lang_code}")
            else:
                print(f"Error al cargar: {translator_path}")
        self.ui.retranslateUi(self)


def main():
    app = QApplication(sys.argv)
    
    window = TestWindow()
    window.setGeometry(100, 100, 600, 500)
    window.show()
    
    print("\n" + "="*60)
    print("✓ Reloj Digital - Aplicación iniciada")
    print("="*60)
    print("\nFuncionalidades:")
    print("  • Selector de idioma (Español/English)")
    print("  • Modo Reloj con alarma configurable")
    print("  • Modo Temporizador/Cronómetro")
    print("  • Controles: Start, Pause, Reset")
    print("\nCierra la ventana para salir...")
    print("="*60 + "\n")
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
