from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLineEdit, QLabel, QGroupBox, QGridLayout,
                             QTableWidget, QTableWidgetItem, QMessageBox,
                             QHeaderView, QTabWidget, QScrollArea, QDialog,
                             QMainWindow, QMenuBar, QAction, QStackedWidget)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, pyqtSignal
import sys
import math

# --- About Dialog (with link and new theme) ---
class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About - Transformer Calculator")
        self.setMinimumSize(600, 500)
        self.setModal(True)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("""
            QDialog { background-color: #2c3e50; color: #ecf0f1; }
            QLabel { color: #ecf0f1; font-family: 'Segoe UI', Arial, sans-serif; }
        """)
        layout = QVBoxLayout()

        title = QLabel("Transformer & Short Circuit Calculator")
        title.setFont(QFont('Segoe UI', 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #e67e22; margin: 20px;")

        version = QLabel("Version 1.0.0")
        version.setFont(QFont('Segoe UI', 14))
        version.setAlignment(Qt.AlignCenter)
        version.setStyleSheet("color: #bdc3c7; margin-bottom: 20px;")

        description = QLabel("""
        Professional Transformer and Short Circuit Calculator
        
        Features:
        • Simple and Detailed Calculations
        • Comprehensive Transformer Rating Tables
        • Fault Current Analysis
        • Loop Impedance Calculations
        • Primary and Secondary Current Analysis
        • Industry Standard Formulas (IEEE/IEC)
        
        Based on Blakley Calculator methodology with advanced 
        electrical engineering calculations for power system analysis.
        
        Developed for electrical engineers, technicians, and 
        power system professionals.
        """)
        description.setFont(QFont('Segoe UI', 12))
        description.setWordWrap(True)
        description.setAlignment(Qt.AlignLeft)
        description.setStyleSheet("margin: 20px; line-height: 1.6;")

        website_link = QLabel('<a href="https://roshannfs.github.io/SRT-/SRT-/" style="color: #f39c12; text-decoration: none;">Visit Roshan Technologies</a>')
        website_link.setFont(QFont('Segoe UI', 12, QFont.Bold))
        website_link.setAlignment(Qt.AlignCenter)
        website_link.setOpenExternalLinks(True)

        copyright_label = QLabel("© 2025 ROSHAN TECHNOLOGIES. I N N O V A T E . E L E V A T E . D O M I N A T E")
        copyright_label.setFont(QFont('Segoe UI', 10))
        copyright_label.setAlignment(Qt.AlignCenter)
        copyright_label.setStyleSheet("color: #7f8c8d; margin-top: 20px;")

        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
            QPushButton { background-color: #34495e; color: #ecf0f1; border: 1px solid #7f8c8d; border-radius: 8px; padding: 10px 30px; font-size: 14px; font-weight: bold; }
            QPushButton:hover { background-color: #4a6278; border: 1px solid #bdc3c7; }
        """)
        close_button.clicked.connect(self.accept)

        layout.addWidget(title)
        layout.addWidget(version)
        layout.addWidget(description)
        layout.addWidget(website_link)
        layout.addWidget(copyright_label)
        layout.addWidget(close_button, alignment=Qt.AlignCenter)
        self.setLayout(layout)

# --- Base Widget for common styles and back button signal ---
class BasePageWidget(QWidget):
    back_pressed = pyqtSignal()

    def get_style(self, name):
        styles = {
            "group": """QGroupBox { background-color: #34495e; border-radius: 12px; border: 1px solid #7f8c8d; padding: 15px; font-size: 14px; font-weight: bold; color: #e67e22; margin-top: 8px; } QGroupBox::title { color: #e67e22; font-size: 16px; padding: 5px; } QLabel { color: #ecf0f1; font-size: 13px; font-weight: bold; }""",
            "input": """QLineEdit { background-color: #2c3e50; color: #ecf0f1; border: 2px solid #7f8c8d; border-radius: 6px; padding: 10px; font-size: 14px; } QLineEdit:focus { border: 2px solid #e67e22; background-color: #4a6278; } QLineEdit::placeholder { color: #95a5a6; font-style: italic; }""",
            "button": """QPushButton { background-color: #e67e22; color: white; border: none; border-radius: 10px; padding: 12px; font-size: 16px; font-weight: bold; margin: 15px 0px; min-height: 25px; } QPushButton:hover { background-color: #f39c12; } QPushButton:pressed { background-color: #d35400; }""",
            "back_button": """QPushButton { background-color: #34495e; color: #ecf0f1; border: 1px solid #7f8c8d; border-radius: 6px; padding: 8px 20px; font-size: 14px; font-weight: bold; } QPushButton:hover { background-color: #4a6278; border: 1px solid #bdc3c7; }""",
            "results": """QLabel { background-color: #233140; color: #f39c12; border: 1px solid #34495e; border-radius: 8px; padding: 15px; font-size: 13px; font-family: 'Consolas', 'Courier New', monospace; font-weight: bold; line-height: 1.5; }""",
            "table": """
                QTableWidget { background-color: #2c3e50; color: #ecf0f1; border: 1px solid #7f8c8d; border-radius: 8px; gridline-color: #34495e; font-size: 12px; } 
                QTableWidget::item { padding: 8px; border-bottom: 1px solid #34495e; } 
                QTableWidget::item:selected { background-color: #e67e22; color: white; font-weight: bold; } 
                QTableWidget::item:alternate { background-color: #34495e; } 
                QHeaderView::section { background-color: #34495e; color: #ecf0f1; padding: 10px; font-weight: bold; border: 1px solid #7f8c8d; font-size: 12px; } 
                QHeaderView::section:hover { background-color: #4a6278; }
            """,
            "tabs": """QTabWidget::pane { border: 1px solid #7f8c8d; background-color: #34495e; border-radius: 8px; } QTabBar::tab { background-color: #2c3e50; color: #ecf0f1; padding: 10px 20px; margin: 2px; border-top-left-radius: 6px; border-top-right-radius: 6px; border: 1px solid #7f8c8d; border-bottom: none; font-size: 12px; font-weight: bold; } QTabBar::tab:selected { background-color: #34495e; } QTabBar::tab:hover { background-color: #4a6278; }"""
        }
        return styles.get(name, "")

# --- Calculation and Table Widgets ---
class SimpleCalculationWidget(BasePageWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea { border: none; background-color: #2c3e50; }
            QScrollBar:vertical { background-color: #34495e; width: 12px; border-radius: 6px; }
            QScrollBar::handle:vertical { background-color: #e67e22; border-radius: 6px; min-height: 20px; }
            QScrollBar::handle:vertical:hover { background-color: #f39c12; }
        """)
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(15)
        content_layout.setContentsMargins(20, 20, 20, 20)

        top_bar_layout = QHBoxLayout()
        back_button = QPushButton("⬅ Back to Menu")
        back_button.setStyleSheet(self.get_style("back_button"))
        back_button.setFixedWidth(170) # FIX: Increased width
        back_button.clicked.connect(self.back_pressed.emit)
        top_bar_layout.addWidget(back_button)
        top_bar_layout.addStretch()
        content_layout.addLayout(top_bar_layout)

        title_layout = QHBoxLayout()
        icon_label = QLabel("🔌")
        icon_label.setFont(QFont('Segoe UI', 36))
        icon_label.setStyleSheet("color: #e67e22;")
        icon_label.setFixedWidth(60)
        title_info = QVBoxLayout()
        title = QLabel("Simple Calculations")
        title.setFont(QFont('Segoe UI', 20, QFont.Bold))
        title.setStyleSheet("color: #e67e22; margin-bottom: 5px;")
        description = QLabel("Basic transformer fault current calculations using impedance voltage method")
        description.setFont(QFont('Segoe UI', 12))
        description.setStyleSheet("color: #bdc3c7; margin-bottom: 15px;")
        description.setWordWrap(True)
        title_info.addWidget(title)
        title_info.addWidget(description)
        title_layout.addWidget(icon_label)
        title_layout.addLayout(title_info)
        title_layout.addStretch()
        content_layout.addLayout(title_layout)

        input_group = QGroupBox("Input Parameters")
        input_group.setStyleSheet(self.get_style("group"))
        input_layout = QGridLayout(input_group)
        input_layout.setSpacing(12)
        input_layout.setColumnStretch(1, 2) # FIX: Allow input column to stretch
        input_layout.addWidget(QLabel("Primary Voltage (V):"), 0, 0)
        self.primary_voltage = QLineEdit(placeholderText="e.g., 11000")
        self.primary_voltage.setStyleSheet(self.get_style("input"))
        input_layout.addWidget(self.primary_voltage, 0, 1)
        input_layout.addWidget(QLabel("Secondary Voltage (V):"), 1, 0)
        self.secondary_voltage = QLineEdit(placeholderText="e.g., 415")
        self.secondary_voltage.setStyleSheet(self.get_style("input"))
        input_layout.addWidget(self.secondary_voltage, 1, 1)
        input_layout.addWidget(QLabel("Transformer Rating (kVA):"), 2, 0)
        self.transformer_rating = QLineEdit(placeholderText="e.g., 1000")
        self.transformer_rating.setStyleSheet(self.get_style("input"))
        input_layout.addWidget(self.transformer_rating, 2, 1)
        input_layout.addWidget(QLabel("Impedance (%):"), 3, 0)
        self.impedance = QLineEdit(placeholderText="e.g., 6")
        self.impedance.setStyleSheet(self.get_style("input"))
        input_layout.addWidget(self.impedance, 3, 1)
        content_layout.addWidget(input_group)
        
        calc_button = QPushButton("Calculate")
        calc_button.setStyleSheet(self.get_style("button"))
        calc_button.clicked.connect(self.calculate)
        content_layout.addWidget(calc_button)
        
        results_group = QGroupBox("Calculation Results")
        results_group.setStyleSheet(self.get_style("group"))
        results_layout = QVBoxLayout(results_group)
        self.results_display = QLabel("Enter values and click Calculate to see results")
        self.results_display.setStyleSheet(self.get_style("results"))
        self.results_display.setWordWrap(True)
        self.results_display.setMinimumHeight(250)
        self.results_display.setAlignment(Qt.AlignTop)
        results_layout.addWidget(self.results_display)
        content_layout.addWidget(results_group)
        content_layout.addStretch()
        
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)
    
    def calculate(self):
        try:
            vp = float(self.primary_voltage.text())
            vs = float(self.secondary_voltage.text())
            va_kva = float(self.transformer_rating.text())
            z_percent = float(self.impedance.text())
            
            if vp > 0 and vs > 0 and va_kva > 0 and z_percent > 0:
                va = va_kva * 1000
                vz = (vp * z_percent) / 100
                secondary_full_load = va / (math.sqrt(3) * vs)
                max_fault_current = (100 / z_percent) * secondary_full_load
                max_fault_kA = max_fault_current / 1000
                primary_current = va / (math.sqrt(3) * vp)
                results_text = f"""📊 CALCULATION RESULTS:\n\n🔹 Impedance Voltage (Vz): {vz:.2f} V\n🔹 Secondary Full Load Current: {secondary_full_load:.2f} A\n🔹 Primary Current: {primary_current:.2f} A\n🔹 Maximum Fault Current: {max_fault_current:.2f} A\n🔹 Maximum Fault Current: {max_fault_kA:.3f} kA\n\n📋 FORMULAS USED:\n• Vz = (Vp × Z%) / 100\n• I_secondary = VA / (√3 × Vs)\n• I_fault_max = (100 / Z%) × I_secondary\n• I_primary = VA / (√3 × Vp)\n\n📝 INPUT VALUES:\n• Primary Voltage: {vp:,.0f} V\n• Secondary Voltage: {vs:,.0f} V\n• Transformer Rating: {va_kva:,.0f} kVA\n• Impedance: {z_percent:.1f}%\n\n✅ ANALYSIS COMPLETE"""
                self.results_display.setText(results_text)
            else:
                self.results_display.setText("⚠️ Please enter all required values greater than zero.")
        except ValueError:
            self.results_display.setText("❌ ERROR: Please enter valid numerical values for all fields.")
        except Exception as e:
            self.results_display.setText(f"❌ UNEXPECTED ERROR: {str(e)}")

class DetailedCalculationWidget(BasePageWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea { border: none; background-color: #2c3e50; }
            QScrollBar:vertical { background-color: #34495e; width: 12px; border-radius: 6px; }
            QScrollBar::handle:vertical { background-color: #e67e22; border-radius: 6px; min-height: 20px; }
            QScrollBar::handle:vertical:hover { background-color: #f39c12; }
        """)
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(15)
        content_layout.setContentsMargins(20, 20, 20, 20)

        top_bar_layout = QHBoxLayout()
        back_button = QPushButton("⬅ Back to Menu")
        back_button.setStyleSheet(self.get_style("back_button"))
        back_button.setFixedWidth(170) # FIX: Increased width
        back_button.clicked.connect(self.back_pressed.emit)
        top_bar_layout.addWidget(back_button)
        top_bar_layout.addStretch()
        content_layout.addLayout(top_bar_layout)

        title_layout = QHBoxLayout()
        icon_label = QLabel("⚡")
        icon_label.setFont(QFont('Segoe UI', 36))
        icon_label.setStyleSheet("color: #e67e22;")
        icon_label.setFixedWidth(60)
        title_info = QVBoxLayout()
        title = QLabel("Detailed Calculations")
        title.setFont(QFont('Segoe UI', 20, QFont.Bold))
        title.setStyleSheet("color: #e67e22; margin-bottom: 5px;")
        description = QLabel("Advanced fault analysis with loop impedance calculations")
        description.setFont(QFont('Segoe UI', 12))
        description.setStyleSheet("color: #bdc3c7; margin-bottom: 15px;")
        description.setWordWrap(True)
        title_info.addWidget(title)
        title_info.addWidget(description)
        title_layout.addWidget(icon_label)
        title_layout.addLayout(title_info)
        title_layout.addStretch()
        content_layout.addLayout(title_layout)

        input_group = QGroupBox("System Parameters")
        input_group.setStyleSheet(self.get_style("group"))
        input_layout = QGridLayout(input_group)
        input_layout.setSpacing(12)
        input_layout.setColumnStretch(1, 2) # FIX: Allow input column to stretch
        input_layout.addWidget(QLabel("Primary Circuit Impedance (Ω):"), 0, 0)
        self.primary_impedance = QLineEdit(placeholderText="Ze + 2R1 (e.g., 0.46)")
        self.primary_impedance.setStyleSheet(self.get_style("input"))
        input_layout.addWidget(self.primary_impedance, 0, 1)
        input_layout.addWidget(QLabel("Secondary Circuit Impedance (Ω):"), 1, 0)
        self.secondary_impedance = QLineEdit(placeholderText="R1 + R2 (e.g., 0.2)")
        self.secondary_impedance.setStyleSheet(self.get_style("input"))
        input_layout.addWidget(self.secondary_impedance, 1, 1)
        input_layout.addWidget(QLabel("Primary Voltage (V):"), 2, 0)
        self.primary_voltage = QLineEdit(placeholderText="Primary voltage")
        self.primary_voltage.setStyleSheet(self.get_style("input"))
        input_layout.addWidget(self.primary_voltage, 2, 1)
        input_layout.addWidget(QLabel("Secondary Voltage (V):"), 3, 0)
        self.secondary_voltage = QLineEdit(placeholderText="Secondary voltage")
        self.secondary_voltage.setStyleSheet(self.get_style("input"))
        input_layout.addWidget(self.secondary_voltage, 3, 1)
        input_layout.addWidget(QLabel("Transformer Rating (VA):"), 4, 0)
        self.transformer_rating = QLineEdit(placeholderText="VA rating")
        self.transformer_rating.setStyleSheet(self.get_style("input"))
        input_layout.addWidget(self.transformer_rating, 4, 1)
        input_layout.addWidget(QLabel("Impedance (%):"), 5, 0)
        self.impedance_percent = QLineEdit(placeholderText="Impedance %")
        self.impedance_percent.setStyleSheet(self.get_style("input"))
        input_layout.addWidget(self.impedance_percent, 5, 1)
        content_layout.addWidget(input_group)

        calc_button = QPushButton("Calculate Loop Impedance")
        calc_button.setStyleSheet(self.get_style("button"))
        calc_button.clicked.connect(self.calculate)
        content_layout.addWidget(calc_button)

        results_group = QGroupBox("Detailed Fault Analysis Results")
        results_group.setStyleSheet(self.get_style("group"))
        results_layout = QVBoxLayout(results_group)
        self.results_display = QLabel("Enter all system parameters and click Calculate to perform detailed fault analysis")
        self.results_display.setStyleSheet(self.get_style("results"))
        self.results_display.setWordWrap(True)
        self.results_display.setMinimumHeight(300)
        self.results_display.setAlignment(Qt.AlignTop)
        results_layout.addWidget(self.results_display)
        content_layout.addWidget(results_group)
        content_layout.addStretch()

        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)

    def calculate(self):
        try:
            zp = float(self.primary_impedance.text())
            r1_r2 = float(self.secondary_impedance.text())
            vp = float(self.primary_voltage.text())
            vs = float(self.secondary_voltage.text())
            va = float(self.transformer_rating.text())
            z_percent = float(self.impedance_percent.text())
            
            if vp > 0 and vs > 0 and va > 0 and z_percent > 0:
                zp_referred = zp * (vs / vp)**2
                zt = (z_percent / 100) * (vs**2 / va)
                zsec = zp_referred + zt + r1_r2
                voltage_to_earth = vs / math.sqrt(3)
                earth_fault_current = voltage_to_earth / zsec
                primary_fault_current = earth_fault_current * (vs / vp)
                secondary_full_load = va / (math.sqrt(3) * vs)
                max_theoretical_fault = (100 / z_percent) * secondary_full_load
                
                results_text = f"""⚡ DETAILED FAULT ANALYSIS RESULTS:\n\n🔸 Total Loop Impedance (Zsec): {zsec:.4f} Ω\n🔸 Earth Fault Current: {earth_fault_current:.2f} A\n🔸 Primary Fault Current: {primary_fault_current:.2f} A\n🔸 Secondary Full Load Current: {secondary_full_load:.2f} A\n🔸 Max Theoretical Fault Current: {max_theoretical_fault:.2f} A (for reference)\n\n📊 IMPEDANCE BREAKDOWN:\n• Primary Circuit (referred to sec.): {zp_referred:.4f} Ω\n• Transformer Impedance (referred to sec.): {zt:.4f} Ω\n• Secondary Circuit (R1 + R2): {r1_r2:.4f} Ω\n\n⚙️ SYSTEM PARAMETERS:\n• Primary Voltage: {vp:,.0f} V\n• Secondary Voltage: {vs:,.0f} V\n• Transformer Rating: {va:,.0f} VA\n• Voltage to Earth: {voltage_to_earth:.1f} V\n\n✅ ANALYSIS COMPLETE"""
                self.results_display.setText(results_text)
            else:
                self.results_display.setText("⚠️ Please enter all required values greater than zero.")
        except ValueError:
            self.results_display.setText("❌ ERROR: Please enter valid numerical values for all fields.")
        except ZeroDivisionError:
            self.results_display.setText("❌ ERROR: Division by zero. Check that voltage and VA values are not zero.")
        except Exception as e:
            self.results_display.setText(f"❌ UNEXPECTED ERROR: {str(e)}")

class TransformerTablesWidget(BasePageWidget):
    def __init__(self, transformer_data):
        super().__init__()
        self.transformer_data = transformer_data
        self.init_ui()
    
    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        top_bar_layout = QHBoxLayout()
        back_button = QPushButton("⬅ Back to Menu")
        back_button.setStyleSheet(self.get_style("back_button"))
        back_button.setFixedWidth(170) # FIX: Increased width
        back_button.clicked.connect(self.back_pressed.emit)
        top_bar_layout.addWidget(back_button)
        top_bar_layout.addStretch()
        main_layout.addLayout(top_bar_layout)
        
        title_layout = QHBoxLayout()
        icon_label = QLabel("📋")
        icon_label.setFont(QFont('Segoe UI', 36))
        icon_label.setStyleSheet("color: #e67e22;")
        icon_label.setFixedWidth(60)
        title_info = QVBoxLayout()
        title = QLabel("Transformer Rating Tables")
        title.setFont(QFont('Segoe UI', 20, QFont.Bold))
        title.setStyleSheet("color: #e67e22; margin-bottom: 5px;")
        description = QLabel("Comprehensive reference data for electrical engineers")
        description.setFont(QFont('Segoe UI', 12))
        description.setStyleSheet("color: #bdc3c7; margin-bottom: 15px;")
        description.setWordWrap(True)
        title_info.addWidget(title)
        title_info.addWidget(description)
        title_layout.addWidget(icon_label)
        title_layout.addLayout(title_info)
        title_layout.addStretch()
        main_layout.addLayout(title_layout)
        
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet(self.get_style("tabs"))
        
        self.create_tabs()
        
        main_layout.addWidget(self.tab_widget)
        
    def create_tabs(self):
        self.tab_widget.addTab(self.create_table_tab('Single Phase 240V Transformers', ['kVA', 'Base Current (A)', 'Max SC (A)'], self.transformer_data['single_phase_240v']), "     Single Phase 240V    " )
        self.tab_widget.addTab(self.create_table_tab('Three Phase 480V Transformers', ['kVA', 'Base Current (A)', 'Max SC (A)'], self.transformer_data['three_phase_480v']), "    Three Phase 480V    ")
        self.tab_widget.addTab(self.create_table_tab('Distribution Transformers 11kV/415V', ['kVA', 'V_pri', 'V_sec', 'I_base (A)', 'Z (%)'], self.transformer_data['distribution_11kv']), "   Distribution 11kV/415V   ")
        self.tab_widget.addTab(self.create_table_tab('Power Transformers', ['MVA', 'Voltage', 'I_hv (A)', 'I_lv (A)', 'Z (%)'], self.transformer_data['power_transformers']), "    Power Transformers    ")

    def create_table_tab(self, title_text, headers, data):
        tab_widget = QWidget()
        layout = QVBoxLayout(tab_widget)
        desc = QLabel(title_text)
        desc.setFont(QFont('Segoe UI', 25, QFont.Bold))
        desc.setStyleSheet("color: #e67e22; margin: 10px;")
        
        table = QTableWidget()
        table.setStyleSheet(self.get_style("table"))
        table.setRowCount(len(data))
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        
        for i, item in enumerate(data):
            for j, value in enumerate(item.values()):
                table.setItem(i, j, QTableWidgetItem(str(value)))
        
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setAlternatingRowColors(True)
        
        layout.addWidget(desc)
        layout.addWidget(table)
        return tab_widget

# --- Main Window using QStackedWidget ---
class TransformerCalculatorMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.transformer_data = self.load_transformer_data()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Transformer & Short Circuit Calculator')
        self.setMinimumSize(1200, 800)
        self.resize(1400, 900)
        self.set_dark_theme()
        self.create_menu_bar()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        self.main_menu_widget = self.create_main_menu_page()
        self.simple_calc_widget = SimpleCalculationWidget()
        self.detailed_calc_widget = DetailedCalculationWidget()
        self.tables_widget = TransformerTablesWidget(self.transformer_data)
        
        self.stacked_widget.addWidget(self.main_menu_widget)
        self.stacked_widget.addWidget(self.simple_calc_widget)
        self.stacked_widget.addWidget(self.detailed_calc_widget)
        self.stacked_widget.addWidget(self.tables_widget)

        self.simple_calc_widget.back_pressed.connect(self.show_main_menu)
        self.detailed_calc_widget.back_pressed.connect(self.show_main_menu)
        self.tables_widget.back_pressed.connect(self.show_main_menu)

    def create_main_menu_page(self):
        main_menu_widget = QWidget()
        main_layout = QVBoxLayout(main_menu_widget)
        main_layout.setSpacing(50)
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.addLayout(self.create_header())
        main_layout.addLayout(self.create_buttons_section())
        main_layout.addStretch()
        main_layout.addLayout(self.create_footer())
        return main_menu_widget
    
    def show_main_menu(self): self.stacked_widget.setCurrentIndex(0)
    def show_simple_calculations(self): self.stacked_widget.setCurrentIndex(1)
    def show_detailed_calculations(self): self.stacked_widget.setCurrentIndex(2)
    def show_transformer_tables(self): self.stacked_widget.setCurrentIndex(3)

    def load_transformer_data(self):
        return {
            "single_phase_240v": [{"kva": 1, "base_current": 4.17, "max_short_circuit": 8.34}, {"kva": 5, "base_current": 20.8, "max_short_circuit": 41.6}, {"kva": 10, "base_current": 41.67, "max_short_circuit": 83.34}, {"kva": 15, "base_current": 62.5, "max_short_circuit": 125.0}, {"kva": 25, "base_current": 104.17, "max_short_circuit": 208.34}, {"kva": 37.5, "base_current": 156.25, "max_short_circuit": 312.5}, {"kva": 50, "base_current": 208.33, "max_short_circuit": 416.66}, {"kva": 75, "base_current": 312.5, "max_short_circuit": 625.0}, {"kva": 100, "base_current": 416.67, "max_short_circuit": 833.34}, {"kva": 167, "base_current": 695.83, "max_short_circuit": 1391.66}, {"kva": 250, "base_current": 1041.67, "max_short_circuit": 2083.34}],
            "three_phase_480v": [{"kva": 3, "base_current": 3.6, "max_short_circuit": 7.2}, {"kva": 6, "base_current": 7.2, "max_short_circuit": 14.4}, {"kva": 9, "base_current": 10.8, "max_short_circuit": 21.6}, {"kva": 15, "base_current": 18.0, "max_short_circuit": 36.0}, {"kva": 30, "base_current": 36.1, "max_short_circuit": 72.2}, {"kva": 45, "base_current": 54.1, "max_short_circuit": 108.2}, {"kva": 75, "base_current": 90.2, "max_short_circuit": 180.4}, {"kva": 112.5, "base_current": 135.3, "max_short_circuit": 270.6}, {"kva": 150, "base_current": 180.4, "max_short_circuit": 360.8}, {"kva": 225, "base_current": 270.6, "max_short_circuit": 541.2}, {"kva": 300, "base_current": 360.8, "max_short_circuit": 721.6}, {"kva": 500, "base_current": 601.4, "max_short_circuit": 1202.8}, {"kva": 750, "base_current": 902.1, "max_short_circuit": 1804.2}, {"kva": 1000, "base_current": 1202.8, "max_short_circuit": 2405.6}],
            "distribution_11kv": [{"kva": 100, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 139.2, "impedance": 4.5}, {"kva": 200, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 278.4, "impedance": 4.5}, {"kva": 315, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 439.0, "impedance": 5.0}, {"kva": 630, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 878.0, "impedance": 5.5}, {"kva": 1000, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 1393.3, "impedance": 6.0}, {"kva": 1250, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 1741.6, "impedance": 6.0}, {"kva": 1600, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 2229.3, "impedance": 6.5}, {"kva": 2000, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 2786.6, "impedance": 6.5}, {"kva": 2500, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 3483.3, "impedance": 7.0}],
            "power_transformers": [{"mva": 12.5, "voltage": "66/11 kV", "base_current_hv": 109.5, "base_current_lv": 656.0, "impedance": 8.0}, {"mva": 20, "voltage": "66/11 kV", "base_current_hv": 175.2, "base_current_lv": 1049.7, "impedance": 8.5}, {"mva": 31.5, "voltage": "66/11 kV", "base_current_hv": 276.0, "base_current_lv": 1653.0, "impedance": 9.0}, {"mva": 100, "voltage": "132/11 kV", "base_current_hv": 437.6, "base_current_lv": 5247.0, "impedance": 12.0}, {"mva": 160, "voltage": "132/11 kV", "base_current_hv": 700.2, "base_current_lv": 8395.2, "impedance": 12.5}, {"mva": 315, "voltage": "400/220 kV", "base_current_hv": 454.7, "base_current_lv": 825.8, "impedance": 14.0}, {"mva": 500, "voltage": "765/400 kV", "base_current_hv": 377.6, "base_current_lv": 721.7, "impedance": 15.0}]
        }

    def set_dark_theme(self):
        self.setStyleSheet("""QMainWindow, QWidget { background-color: #2c3e50; color: #ecf0f1; font-family: 'Segoe UI', Arial, sans-serif; }""")
        
    def create_menu_bar(self):
        menubar = self.menuBar()
        menubar.setStyleSheet("""
            QMenuBar { background-color: #34495e; color: #ecf0f1; font-size: 14px; font-weight: bold; padding: 5px; }
            QMenuBar::item { padding: 8px 15px; margin: 2px; }
            QMenuBar::item:selected { background-color: #4a6278; border-radius: 5px; }
            QMenu { background-color: #34495e; color: #ecf0f1; border: 1px solid #7f8c8d; }
            QMenu::item:selected { background-color: #e67e22; }
        """)
        help_menu = menubar.addMenu('Help')
        about_action = QAction('About', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def show_about(self):
        about_dialog = AboutDialog(self)
        about_dialog.exec_()

    def create_header(self):
        header_layout = QVBoxLayout()
        header_layout.setSpacing(30)
        title_row = QHBoxLayout()
        logo_label = QLabel("SRT")
        logo_label.setFixedSize(120, 120)
        logo_label.setStyleSheet("""QLabel { background-color: #34495e; border: 4px solid #ecf0f1; border-radius: 60px; }""")
        logo_label.setAlignment(Qt.AlignCenter)
        logo_label.setFont(QFont('Segoe UI', 28, QFont.Bold))
        title_section = QVBoxLayout()
        title_section.setSpacing(10)
        title_label = QLabel('Transformer & Short Circuit Calculator')
        title_label.setFont(QFont('Segoe UI', 42, QFont.Bold))
        title_label.setStyleSheet("color: #ecf0f1; margin-left: 40px;")
        subtitle_label = QLabel('Professional Power System Analysis Tool')
        subtitle_label.setFont(QFont('Segoe UI', 20))
        subtitle_label.setStyleSheet("color: #bdc3c7; margin-left: 40px;")
        version_label = QLabel('Version 1.0.0')
        version_label.setFont(QFont('Segoe UI', 16))
        version_label.setStyleSheet("color: #e67e22; margin-left: 40px;")
        title_section.addWidget(title_label)
        title_section.addWidget(subtitle_label)
        title_section.addWidget(version_label)
        title_row.addWidget(logo_label)
        title_row.addLayout(title_section)
        title_row.addStretch()
        header_layout.addLayout(title_row)
        return header_layout

    def create_buttons_section(self):
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(50)
        section_title = QLabel("Select Calculation Type")
        section_title.setFont(QFont('Segoe UI', 28, QFont.Bold))
        section_title.setAlignment(Qt.AlignCenter)
        section_title.setStyleSheet("color: #e67e22; margin: 40px 0px;")
        buttons_layout.addWidget(section_title)
        buttons_grid = QHBoxLayout()
        buttons_grid.setSpacing(60)
        buttons_grid.setAlignment(Qt.AlignCenter)
        simple_button = self.create_styled_button("🔌", "Simple Calculations", self.show_simple_calculations)
        detailed_button = self.create_styled_button("⚡", "Detailed Calculations", self.show_detailed_calculations)
        tables_button = self.create_styled_button("📋", "Transformer Tables", self.show_transformer_tables)
        buttons_grid.addWidget(simple_button)
        buttons_grid.addWidget(detailed_button)
        buttons_grid.addWidget(tables_button)
        buttons_layout.addLayout(buttons_grid)
        return buttons_layout

    def create_styled_button(self, icon, title, callback):
        button = QPushButton()
        button.setFixedSize(300, 200)
        button.setCursor(Qt.PointingHandCursor)
        button_layout = QVBoxLayout(button)
        button_layout.setSpacing(20)
        button_layout.setAlignment(Qt.AlignCenter)
        icon_label = QLabel(icon)
        icon_label.setFont(QFont('Segoe UI', 72))
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet("color: #e67e22; background: transparent; border: none;")
        title_label = QLabel(title)
        title_label.setFont(QFont('Segoe UI', 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #ecf0f1; background: transparent; border: none;")
        title_label.setWordWrap(True)
        button_layout.addWidget(icon_label)
        button_layout.addWidget(title_label)
        button.setStyleSheet("""
            QPushButton { background-color: #34495e; border: 2px solid #7f8c8d; border-radius: 25px; padding: 20px; }
            QPushButton:hover { background-color: #4a6278; border: 2px solid #e67e22; }
            QPushButton:pressed { background-color: #2c3e50; }
        """)
        button.clicked.connect(callback)
        return button

    def create_footer(self):
        footer_layout = QHBoxLayout()
        footer_text = QLabel('<a href="https://roshannfs.github.io/SRT-/SRT-/" style="color: #7f8c8d; text-decoration: none;">© 2025 ROSHAN TECHNOLOGIES - I N N O V A T E . E L E V A T E . D O M I N A T E</a>')
        footer_text.setFont(QFont('Segoe UI', 14))
        footer_text.setAlignment(Qt.AlignCenter)
        footer_text.setStyleSheet("margin-top: 50px;")
        footer_text.setOpenExternalLinks(True)
        footer_layout.addWidget(footer_text)
        return footer_layout

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setApplicationName("Transformer Calculator")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("ROSHAN TECHNOLOGIES")
    window = TransformerCalculatorMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()