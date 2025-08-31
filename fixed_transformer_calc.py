from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLineEdit, QLabel, QGroupBox, QGridLayout,
                             QTableWidget, QTableWidgetItem, QComboBox, QMessageBox,
                             QHeaderView, QTabWidget, QScrollArea, QDialog, QTextEdit,
                             QMainWindow, QMenuBar, QAction, QSplitter, QFrame)
from PyQt5.QtGui import QFont, QPalette, QColor, QPixmap, QIcon
from PyQt5.QtCore import Qt, QTimer
import sys
import json
import math

class AboutDialog(QDialog):
    """About dialog for the application"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About - GE Transformer Calculator")
        self.setFixedSize(600, 400)
        self.setModal(True)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #0a2543;
                color: white;
            }
            QLabel {
                color: white;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
        """)
        
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("GE Transformer & Short Circuit Calculator")
        title.setFont(QFont('Segoe UI', 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #4da6ff; margin: 20px;")
        
        # Version
        version = QLabel("Version 2.0")
        version.setFont(QFont('Segoe UI', 14))
        version.setAlignment(Qt.AlignCenter)
        version.setStyleSheet("color: #b0b0b0; margin-bottom: 20px;")
        
        # Description
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
        
        # Copyright
        copyright = QLabel("© 2025 ROSHAN TECHNOLOGIES. All rights reserved.")
        copyright.setFont(QFont('Segoe UI', 10))
        copyright.setAlignment(Qt.AlignCenter)
        copyright.setStyleSheet("color: #888888; margin-top: 20px;")
        
        # Close button
        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #2771b3;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 30px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3a8bc7;
            }
        """)
        close_button.clicked.connect(self.accept)
        
        layout.addWidget(title)
        layout.addWidget(version)
        layout.addWidget(description)
        layout.addWidget(copyright)
        layout.addWidget(close_button, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)

class SimpleCalculationDialog(QDialog):
    """Dialog for Simple Calculations"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Simple Calculations - Transformer Analysis")
        self.setMinimumSize(800, 700)
        self.resize(800, 700)
        self.setModal(True)
        self.init_ui()
    
    def init_ui(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #0a2543;
                color: white;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
        """)
        
        # Create scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: #0a2543;
            }
            QScrollBar:vertical {
                background-color: #1e4a73;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background-color: #4da6ff;
                border-radius: 6px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #3a8bc7;
            }
        """)
        
        # Content widget
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(15)
        content_layout.setContentsMargins(20, 20, 20, 20)
        
        # Title section
        title_layout = QHBoxLayout()
        
        # Icon
        icon_label = QLabel("🔌")
        icon_label.setFont(QFont('Segoe UI', 36))
        icon_label.setStyleSheet("color: #4da6ff;")
        icon_label.setFixedWidth(60)
        
        # Title and description
        title_info = QVBoxLayout()
        title = QLabel("Simple Calculations")
        title.setFont(QFont('Segoe UI', 20, QFont.Bold))
        title.setStyleSheet("color: #4da6ff; margin-bottom: 5px;")
        
        description = QLabel("Basic transformer fault current calculations using impedance voltage method")
        description.setFont(QFont('Segoe UI', 12))
        description.setStyleSheet("color: #b0b0b0; margin-bottom: 15px;")
        description.setWordWrap(True)
        
        title_info.addWidget(title)
        title_info.addWidget(description)
        
        title_layout.addWidget(icon_label)
        title_layout.addLayout(title_info)
        title_layout.addStretch()
        
        # Input fields group
        input_group = QGroupBox("Input Parameters")
        input_group.setStyleSheet(self.get_group_style())
        input_layout = QGridLayout()
        input_layout.setSpacing(12)
        
        # Primary Voltage
        input_layout.addWidget(QLabel("Primary Voltage (V):"), 0, 0)
        self.primary_voltage = QLineEdit()
        self.primary_voltage.setPlaceholderText("e.g., 11000")
        self.primary_voltage.setStyleSheet(self.get_input_style())
        input_layout.addWidget(self.primary_voltage, 0, 1)
        
        # Secondary Voltage
        input_layout.addWidget(QLabel("Secondary Voltage (V):"), 1, 0)
        self.secondary_voltage = QLineEdit()
        self.secondary_voltage.setPlaceholderText("e.g., 415")
        self.secondary_voltage.setStyleSheet(self.get_input_style())
        input_layout.addWidget(self.secondary_voltage, 1, 1)
        
        # Transformer Rating
        input_layout.addWidget(QLabel("Transformer Rating (kVA):"), 2, 0)
        self.transformer_rating = QLineEdit()
        self.transformer_rating.setPlaceholderText("e.g., 1000")
        self.transformer_rating.setStyleSheet(self.get_input_style())
        input_layout.addWidget(self.transformer_rating, 2, 1)
        
        # Impedance
        input_layout.addWidget(QLabel("Impedance (%):"), 3, 0)
        self.impedance = QLineEdit()
        self.impedance.setPlaceholderText("e.g., 6")
        self.impedance.setStyleSheet(self.get_input_style())
        input_layout.addWidget(self.impedance, 3, 1)
        
        input_group.setLayout(input_layout)
        
        # Calculate button
        calc_button = QPushButton("Calculate")
        calc_button.setStyleSheet(self.get_button_style())
        calc_button.clicked.connect(self.calculate)
        
        # Results display
        results_group = QGroupBox("Calculation Results")
        results_group.setStyleSheet(self.get_group_style())
        results_layout = QVBoxLayout()
        
        self.results_display = QLabel("Enter values and click Calculate to see results")
        self.results_display.setStyleSheet(self.get_results_style())
        self.results_display.setWordWrap(True)
        self.results_display.setMinimumHeight(250)
        self.results_display.setAlignment(Qt.AlignTop)
        
        results_layout.addWidget(self.results_display)
        results_group.setLayout(results_layout)
        
        # Close button
        close_button = QPushButton("Close")
        close_button.setStyleSheet(self.get_close_button_style())
        close_button.clicked.connect(self.accept)
        
        # Add all to content layout
        content_layout.addLayout(title_layout)
        content_layout.addWidget(input_group)
        content_layout.addWidget(calc_button)
        content_layout.addWidget(results_group)
        content_layout.addWidget(close_button, alignment=Qt.AlignCenter)
        
        # Set content widget to scroll area
        scroll_area.setWidget(content_widget)
        
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(scroll_area)
        
        self.setLayout(main_layout)
    
    def calculate(self):
        """Perform simple calculations"""
        try:
            # Get input values
            vp = float(self.primary_voltage.text()) if self.primary_voltage.text() else 0
            vs = float(self.secondary_voltage.text()) if self.secondary_voltage.text() else 0
            va_kva = float(self.transformer_rating.text()) if self.transformer_rating.text() else 0
            z_percent = float(self.impedance.text()) if self.impedance.text() else 0
            
            if vp > 0 and vs > 0 and va_kva > 0 and z_percent > 0:
                # Convert kVA to VA
                va = va_kva * 1000
                
                # Formula 1: Impedance Voltage
                vz = (vp * z_percent) / 100
                
                # Formula 2: Secondary Full Load Current (3-phase)
                secondary_full_load = va / (math.sqrt(3) * vs)
                
                # Formula 3: Maximum Fault Current
                max_fault_current = (100 / z_percent) * secondary_full_load
                max_fault_kA = max_fault_current / 1000
                
                # Formula 4: Primary Current
                primary_current = va / (math.sqrt(3) * vp)
                
                # Display results
                results_text = f"""📊 CALCULATION RESULTS:

🔹 Impedance Voltage (Vz): {vz:.2f} V
🔹 Secondary Full Load Current: {secondary_full_load:.2f} A
🔹 Primary Current: {primary_current:.2f} A
🔹 Maximum Fault Current: {max_fault_current:.2f} A
🔹 Maximum Fault Current: {max_fault_kA:.3f} kA

📋 FORMULAS USED:
• Vz = (Vp × Z%) / 100
• I_secondary = VA / (√3 × Vs)
• I_fault_max = (100 / Z%) × I_secondary
• I_primary = VA / (√3 × Vp)

📝 INPUT VALUES:
• Primary Voltage: {vp:,.0f} V
• Secondary Voltage: {vs:,.0f} V  
• Transformer Rating: {va_kva:,.0f} kVA
• Impedance: {z_percent:.1f}%

✅ ANALYSIS COMPLETE
All calculations based on IEEE/IEC standards."""
                
                self.results_display.setText(results_text)
            else:
                self.results_display.setText("⚠️ Please enter all required values:\n• Primary Voltage\n• Secondary Voltage\n• Transformer Rating (kVA)\n• Impedance (%)")
                
        except ValueError:
            self.results_display.setText("❌ ERROR: Please enter valid numerical values")
        except Exception as e:
            self.results_display.setText(f"❌ ERROR: {str(e)}")
    
    def get_group_style(self):
        return """
            QGroupBox {
                background-color: #1e4a73;
                border-radius: 12px;
                border: 2px solid #2771b3;
                padding: 15px;
                font-size: 14px;
                font-weight: bold;
                color: #4da6ff;
                margin: 8px;
            }
            QGroupBox::title {
                color: #4da6ff;
                font-size: 16px;
                font-weight: bold;
                padding: 5px;
            }
            QLabel {
                color: white;
                font-size: 13px;
                font-weight: bold;
            }
        """
    
    def get_input_style(self):
        return """
            QLineEdit {
                background-color: #2771b3;
                color: white;
                border: 2px solid #3a8bc7;
                border-radius: 6px;
                padding: 10px;
                font-size: 14px;
                font-family: 'Segoe UI', Arial, sans-serif;
                min-height: 18px;
            }
            QLineEdit:focus {
                border: 2px solid #4da6ff;
                background-color: #3a8bc7;
            }
            QLineEdit::placeholder {
                color: #b0b0b0;
                font-style: italic;
            }
        """
    
    def get_button_style(self):
        return """
            QPushButton {
                background-color: #4da6ff;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px;
                font-size: 16px;
                font-weight: bold;
                font-family: 'Segoe UI', Arial, sans-serif;
                margin: 15px 0px;
                min-height: 25px;
            }
            QPushButton:hover {
                background-color: #3a8bc7;
            }
            QPushButton:pressed {
                background-color: #2771b3;
            }
        """
    
    def get_close_button_style(self):
        return """
            QPushButton {
                background-color: #2771b3;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 20px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3a8bc7;
            }
        """
    
    def get_results_style(self):
        return """
            QLabel {
                background-color: #0d3a5f;
                color: #4da6ff;
                border: 2px solid #2771b3;
                border-radius: 8px;
                padding: 15px;
                font-size: 13px;
                font-family: 'Consolas', 'Courier New', monospace;
                font-weight: bold;
                line-height: 1.5;
            }
        """

class DetailedCalculationDialog(QDialog):
    """Dialog for Detailed Calculations"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Detailed Calculations - Loop Impedance Analysis")
        self.setMinimumSize(850, 800)
        self.resize(850, 800)
        self.setModal(True)
        self.init_ui()
    
    def init_ui(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #0a2543;
                color: white;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
        """)
        
        # Create scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: #0a2543;
            }
            QScrollBar:vertical {
                background-color: #1e4a73;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background-color: #4da6ff;
                border-radius: 6px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #3a8bc7;
            }
        """)
        
        # Content widget
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(15)
        content_layout.setContentsMargins(20, 20, 20, 20)
        
        # Title section
        title_layout = QHBoxLayout()
        
        # Icon
        icon_label = QLabel("⚡")
        icon_label.setFont(QFont('Segoe UI', 36))
        icon_label.setStyleSheet("color: #4da6ff;")
        icon_label.setFixedWidth(60)
        
        # Title and description
        title_info = QVBoxLayout()
        title = QLabel("Detailed Calculations")
        title.setFont(QFont('Segoe UI', 20, QFont.Bold))
        title.setStyleSheet("color: #4da6ff; margin-bottom: 5px;")
        
        description = QLabel("Advanced fault analysis with loop impedance calculations")
        description.setFont(QFont('Segoe UI', 12))
        description.setStyleSheet("color: #b0b0b0; margin-bottom: 15px;")
        description.setWordWrap(True)
        
        title_info.addWidget(title)
        title_info.addWidget(description)
        
        title_layout.addWidget(icon_label)
        title_layout.addLayout(title_info)
        title_layout.addStretch()
        
        # Input fields group
        input_group = QGroupBox("System Parameters")
        input_group.setStyleSheet(self.get_group_style())
        input_layout = QGridLayout()
        input_layout.setSpacing(12)
        
        # Primary Circuit Impedance
        input_layout.addWidget(QLabel("Primary Circuit Impedance (Ω):"), 0, 0)
        self.primary_impedance = QLineEdit()
        self.primary_impedance.setPlaceholderText("Ze + 2R1 (e.g., 0.46)")
        self.primary_impedance.setStyleSheet(self.get_input_style())
        input_layout.addWidget(self.primary_impedance, 0, 1)
        
        # Secondary Circuit Impedance
        input_layout.addWidget(QLabel("Secondary Circuit Impedance (Ω):"), 1, 0)
        self.secondary_impedance = QLineEdit()
        self.secondary_impedance.setPlaceholderText("R1 + R2 (e.g., 0.2)")
        self.secondary_impedance.setStyleSheet(self.get_input_style())
        input_layout.addWidget(self.secondary_impedance, 1, 1)
        
        # Primary Voltage
        input_layout.addWidget(QLabel("Primary Voltage (V):"), 2, 0)
        self.primary_voltage = QLineEdit()
        self.primary_voltage.setPlaceholderText("Primary voltage")
        self.primary_voltage.setStyleSheet(self.get_input_style())
        input_layout.addWidget(self.primary_voltage, 2, 1)
        
        # Secondary Voltage
        input_layout.addWidget(QLabel("Secondary Voltage (V):"), 3, 0)
        self.secondary_voltage = QLineEdit()
        self.secondary_voltage.setPlaceholderText("Secondary voltage")
        self.secondary_voltage.setStyleSheet(self.get_input_style())
        input_layout.addWidget(self.secondary_voltage, 3, 1)
        
        # Transformer Rating
        input_layout.addWidget(QLabel("Transformer Rating (VA):"), 4, 0)
        self.transformer_rating = QLineEdit()
        self.transformer_rating.setPlaceholderText("VA rating")
        self.transformer_rating.setStyleSheet(self.get_input_style())
        input_layout.addWidget(self.transformer_rating, 4, 1)
        
        # Impedance Percentage
        input_layout.addWidget(QLabel("Impedance (%):"), 5, 0)
        self.impedance_percent = QLineEdit()
        self.impedance_percent.setPlaceholderText("Impedance %")
        self.impedance_percent.setStyleSheet(self.get_input_style())
        input_layout.addWidget(self.impedance_percent, 5, 1)
        
        input_group.setLayout(input_layout)
        
        # Calculate button
        calc_button = QPushButton("Calculate Loop Impedance")
        calc_button.setStyleSheet(self.get_button_style())
        calc_button.clicked.connect(self.calculate)
        
        # Results display
        results_group = QGroupBox("Detailed Fault Analysis Results")
        results_group.setStyleSheet(self.get_group_style())
        results_layout = QVBoxLayout()
        
        self.results_display = QLabel("Enter all system parameters and click Calculate to perform detailed fault analysis")
        self.results_display.setStyleSheet(self.get_results_style())
        self.results_display.setWordWrap(True)
        self.results_display.setMinimumHeight(300)
        self.results_display.setAlignment(Qt.AlignTop)
        
        results_layout.addWidget(self.results_display)
        results_group.setLayout(results_layout)
        
        # Close button
        close_button = QPushButton("Close")
        close_button.setStyleSheet(self.get_close_button_style())
        close_button.clicked.connect(self.accept)
        
        # Add all to content layout
        content_layout.addLayout(title_layout)
        content_layout.addWidget(input_group)
        content_layout.addWidget(calc_button)
        content_layout.addWidget(results_group)
        content_layout.addWidget(close_button, alignment=Qt.AlignCenter)
        
        # Set content widget to scroll area
        scroll_area.setWidget(content_widget)
        
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(scroll_area)
        
        self.setLayout(main_layout)
    
    def calculate(self):
        """Perform detailed calculations with loop impedance"""
        try:
            # Get input values
            zp = float(self.primary_impedance.text()) if self.primary_impedance.text() else 0
            r1_r2 = float(self.secondary_impedance.text()) if self.secondary_impedance.text() else 0
            vp = float(self.primary_voltage.text()) if self.primary_voltage.text() else 0
            vs = float(self.secondary_voltage.text()) if self.secondary_voltage.text() else 0
            va = float(self.transformer_rating.text()) if self.transformer_rating.text() else 0
            z_percent = float(self.impedance_percent.text()) if self.impedance_percent.text() else 0
            
            if all([zp, vp, vs, va, z_percent]):
                # Formula: Loop Impedance Calculation (from Excel)
                # Zsec = Zp × (Vs²/Vp) × (Z%/100) × (1/VA) + (R1 + R2)
                zsec = zp * (vs**2 / vp) * (z_percent / 100) * (1 / va) + r1_r2
                
                # Formula: Earth Fault Current
                # For single phase: Uo = Vs, For three phase: Uo = Vs/√3
                voltage_to_earth = vs / math.sqrt(3)  # Three-phase system
                earth_fault_current = voltage_to_earth / zsec
                
                # Formula: Primary Fault Current
                primary_fault_current = earth_fault_current * (vs / vp)
                
                # Secondary Full Load Current
                secondary_full_load = va / (math.sqrt(3) * vs)
                
                # Maximum theoretical fault current (without loop impedance)
                max_theoretical_fault = (100 / z_percent) * secondary_full_load
                
                # Display detailed results
                results_text = f"""⚡ DETAILED FAULT ANALYSIS RESULTS:

🔸 Total Loop Impedance (Zsec): {zsec:.4f} Ω
🔸 Earth Fault Current: {earth_fault_current:.2f} A
🔸 Primary Fault Current: {primary_fault_current:.2f} A
🔸 Secondary Full Load Current: {secondary_full_load:.2f} A
🔸 Max Theoretical Fault Current: {max_theoretical_fault:.2f} A

📊 IMPEDANCE BREAKDOWN:
• Primary Circuit (Ze + 2R1): {zp:.3f} Ω
• Secondary Circuit (R1 + R2): {r1_r2:.3f} Ω
• Transformer Impedance: {z_percent:.1f}%

📐 FORMULAS USED:
• Zsec = Zp × (Vs²/Vp) × (Z%/100) × (1/VA) + (R1+R2)
• Ia = Voltage_to_Earth / Zsec
• I_primary = Ia × (Vs/Vp)

⚙️ SYSTEM PARAMETERS:
• Primary Voltage: {vp:,.0f} V
• Secondary Voltage: {vs:,.0f} V
• Transformer Rating: {va:,.0f} VA
• Voltage to Earth: {voltage_to_earth:.1f} V

✅ ANALYSIS COMPLETE
Based on BS7671:2008 and IEC standards."""
                
                self.results_display.setText(results_text)
            else:
                self.results_display.setText("⚠️ Please enter all required values for detailed fault current analysis:\n• Primary Circuit Impedance (Ω)\n• Secondary Circuit Impedance (Ω)\n• Primary Voltage (V)\n• Secondary Voltage (V)\n• Transformer Rating (VA)\n• Impedance (%)")
                
        except ValueError:
            self.results_display.setText("❌ ERROR: Please enter valid numerical values")
        except ZeroDivisionError:
            self.results_display.setText("❌ ERROR: Division by zero - check impedance values")
        except Exception as e:
            self.results_display.setText(f"❌ ERROR: {str(e)}")
    
    def get_group_style(self):
        return """
            QGroupBox {
                background-color: #1e4a73;
                border-radius: 12px;
                border: 2px solid #2771b3;
                padding: 15px;
                font-size: 14px;
                font-weight: bold;
                color: #4da6ff;
                margin: 8px;
            }
            QGroupBox::title {
                color: #4da6ff;
                font-size: 16px;
                font-weight: bold;
                padding: 5px;
            }
            QLabel {
                color: white;
                font-size: 13px;
                font-weight: bold;
            }
        """
    
    def get_input_style(self):
        return """
            QLineEdit {
                background-color: #2771b3;
                color: white;
                border: 2px solid #3a8bc7;
                border-radius: 6px;
                padding: 10px;
                font-size: 14px;
                font-family: 'Segoe UI', Arial, sans-serif;
                min-height: 18px;
            }
            QLineEdit:focus {
                border: 2px solid #4da6ff;
                background-color: #3a8bc7;
            }
            QLineEdit::placeholder {
                color: #b0b0b0;
                font-style: italic;
            }
        """
    
    def get_button_style(self):
        return """
            QPushButton {
                background-color: #4da6ff;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px;
                font-size: 16px;
                font-weight: bold;
                font-family: 'Segoe UI', Arial, sans-serif;
                margin: 15px 0px;
                min-height: 25px;
            }
            QPushButton:hover {
                background-color: #3a8bc7;
            }
            QPushButton:pressed {
                background-color: #2771b3;
            }
        """
    
    def get_close_button_style(self):
        return """
            QPushButton {
                background-color: #2771b3;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 20px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3a8bc7;
            }
        """
    
    def get_results_style(self):
        return """
            QLabel {
                background-color: #0d3a5f;
                color: #4da6ff;
                border: 2px solid #2771b3;
                border-radius: 8px;
                padding: 15px;
                font-size: 13px;
                font-family: 'Consolas', 'Courier New', monospace;
                font-weight: bold;
                line-height: 1.5;
            }
        """

class TransformerTablesDialog(QDialog):
    """Dialog for Transformer Tables"""
    def __init__(self, transformer_data, parent=None):
        super().__init__(parent)
        self.transformer_data = transformer_data
        self.setWindowTitle("Transformer Rating Tables - Professional Reference")
        self.setMinimumSize(1000, 700)
        self.resize(1200, 800)
        self.setModal(True)
        self.init_ui()
    
    def init_ui(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #0a2543;
                color: white;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Title section
        title_layout = QHBoxLayout()
        
        # Icon
        icon_label = QLabel("📋")
        icon_label.setFont(QFont('Segoe UI', 36))
        icon_label.setStyleSheet("color: #4da6ff;")
        icon_label.setFixedWidth(60)
        
        # Title and description
        title_info = QVBoxLayout()
        title = QLabel("Transformer Rating Tables")
        title.setFont(QFont('Segoe UI', 20, QFont.Bold))
        title.setStyleSheet("color: #4da6ff; margin-bottom: 5px;")
        
        description = QLabel("Comprehensive reference data for electrical engineers")
        description.setFont(QFont('Segoe UI', 12))
        description.setStyleSheet("color: #b0b0b0; margin-bottom: 15px;")
        description.setWordWrap(True)
        
        title_info.addWidget(title)
        title_info.addWidget(description)
        
        title_layout.addWidget(icon_label)
        title_layout.addLayout(title_info)
        title_layout.addStretch()
        
        # Tab widget for different transformer types
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid #2771b3;
                background-color: #1e4a73;
                border-radius: 8px;
            }
            QTabBar::tab {
                background-color: #2771b3;
                color: white;
                padding: 10px 20px;
                margin: 2px;
                border-radius: 6px;
                font-size: 12px;
                font-weight: bold;
            }
            QTabBar::tab:selected {
                background-color: #3a8bc7;
            }
            QTabBar::tab:hover {
                background-color: #4da6ff;
            }
        """)
        
        # Create tabs for each transformer type
        self.create_single_phase_tab()
        self.create_three_phase_tab()
        self.create_distribution_tab()
        self.create_power_transformer_tab()
        
        # Close button
        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #2771b3;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 20px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3a8bc7;
            }
        """)
        close_button.clicked.connect(self.accept)
        
        layout.addLayout(title_layout)
        layout.addWidget(self.tab_widget, 1)
        layout.addWidget(close_button, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)
    
    def create_single_phase_tab(self):
        """Create single phase transformer table"""
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Description
        desc = QLabel('Single Phase 240V Transformers - Standard Ratings')
        desc.setFont(QFont('Segoe UI', 14, QFont.Bold))
        desc.setStyleSheet("color: #4da6ff; margin: 10px;")
        
        # Table
        table = QTableWidget()
        table.setStyleSheet(self.get_table_style())
        
        data = self.transformer_data['single_phase_240v']
        table.setRowCount(len(data))
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(['kVA Rating', 'Base Current (A)', 'Max Short Circuit (A)'])
        
        for i, item in enumerate(data):
            table.setItem(i, 0, QTableWidgetItem(str(item['kva'])))
            table.setItem(i, 1, QTableWidgetItem(str(item['base_current'])))
            table.setItem(i, 2, QTableWidgetItem(str(item['max_short_circuit'])))
        
        # Auto-resize columns
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setAlternatingRowColors(True)
        
        layout.addWidget(desc)
        layout.addWidget(table)
        tab.setLayout(layout)
        
        self.tab_widget.addTab(tab, "Single Phase 240V")
    
    def create_three_phase_tab(self):
        """Create three phase transformer table"""
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Description
        desc = QLabel('Three Phase 480V Transformers - Industrial Standard Ratings')
        desc.setFont(QFont('Segoe UI', 14, QFont.Bold))
        desc.setStyleSheet("color: #4da6ff; margin: 10px;")
        
        # Table
        table = QTableWidget()
        table.setStyleSheet(self.get_table_style())
        
        data = self.transformer_data['three_phase_480v']
        table.setRowCount(len(data))
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(['kVA Rating', 'Base Current (A)', 'Max Short Circuit (A)'])
        
        for i, item in enumerate(data):
            table.setItem(i, 0, QTableWidgetItem(str(item['kva'])))
            table.setItem(i, 1, QTableWidgetItem(str(item['base_current'])))
            table.setItem(i, 2, QTableWidgetItem(str(item['max_short_circuit'])))
        
        # Auto-resize columns
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setAlternatingRowColors(True)
        
        layout.addWidget(desc)
        layout.addWidget(table)
        tab.setLayout(layout)
        
        self.tab_widget.addTab(tab, "Three Phase 480V")
    
    def create_distribution_tab(self):
        """Create distribution transformer table"""
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Description
        desc = QLabel('Distribution Transformers 11kV/415V - Utility Grade')
        desc.setFont(QFont('Segoe UI', 14, QFont.Bold))
        desc.setStyleSheet("color: #4da6ff; margin: 10px;")
        
        # Table
        table = QTableWidget()
        table.setStyleSheet(self.get_table_style())
        
        data = self.transformer_data['distribution_11kv']
        table.setRowCount(len(data))
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(['kVA Rating', 'Primary Voltage (V)', 'Secondary Voltage (V)', 'Base Current (A)', 'Impedance (%)'])
        
        for i, item in enumerate(data):
            table.setItem(i, 0, QTableWidgetItem(str(item['kva'])))
            table.setItem(i, 1, QTableWidgetItem(f"{item['primary_voltage']:,}"))
            table.setItem(i, 2, QTableWidgetItem(str(item['secondary_voltage'])))
            table.setItem(i, 3, QTableWidgetItem(str(item['base_current'])))
            table.setItem(i, 4, QTableWidgetItem(str(item['impedance'])))
        
        # Auto-resize columns
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setAlternatingRowColors(True)
        
        layout.addWidget(desc)
        layout.addWidget(table)
        tab.setLayout(layout)
        
        self.tab_widget.addTab(tab, "Distribution 11kV/415V")
    
    def create_power_transformer_tab(self):
        """Create power transformer table"""
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Description
        desc = QLabel('Power Transformers - Transmission & Sub-transmission')
        desc.setFont(QFont('Segoe UI', 14, QFont.Bold))
        desc.setStyleSheet("color: #4da6ff; margin: 10px;")
        
        # Table
        table = QTableWidget()
        table.setStyleSheet(self.get_table_style())
        
        data = self.transformer_data['power_transformers']
        table.setRowCount(len(data))
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(['MVA Rating', 'Voltage Levels', 'HV Current (A)', 'LV Current (A)', 'Impedance (%)'])
        
        for i, item in enumerate(data):
            table.setItem(i, 0, QTableWidgetItem(str(item['mva'])))
            table.setItem(i, 1, QTableWidgetItem(item['voltage']))
            table.setItem(i, 2, QTableWidgetItem(str(item['base_current_hv'])))
            table.setItem(i, 3, QTableWidgetItem(str(item['base_current_lv'])))
            table.setItem(i, 4, QTableWidgetItem(str(item['impedance'])))
        
        # Auto-resize columns
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setAlternatingRowColors(True)
        
        layout.addWidget(desc)
        layout.addWidget(table)
        tab.setLayout(layout)
        
        self.tab_widget.addTab(tab, "Power Transformers")
    
    def get_table_style(self):
        """Return enhanced stylesheet for tables"""
        return """
            QTableWidget {
                background-color: #1e4a73;
                color: white;
                border: 2px solid #3a8bc7;
                border-radius: 8px;
                gridline-color: #2771b3;
                font-size: 12px;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #2771b3;
            }
            QTableWidget::item:selected {
                background-color: #3a8bc7;
                font-weight: bold;
            }
            QTableWidget::item:alternate {
                background-color: #1a4066;
            }
            QHeaderView::section {
                background-color: #2771b3;
                color: white;
                padding: 10px;
                font-weight: bold;
                border: 1px solid #3a8bc7;
                font-size: 12px;
            }
            QHeaderView::section:hover {
                background-color: #3a8bc7;
            }
        """

class TransformerCalculatorMainWindow(QMainWindow):
    """Main window with buttons to open calculation dialogs"""
    def __init__(self):
        super().__init__()
        self.transformer_data = self.load_transformer_data()
        self.init_ui()
    
    def load_transformer_data(self):
        """Load transformer rating data"""
        return {
            "single_phase_240v": [
                {"kva": 1, "base_current": 4.17, "max_short_circuit": 8.34},
                {"kva": 5, "base_current": 20.8, "max_short_circuit": 41.6},
                {"kva": 10, "base_current": 41.67, "max_short_circuit": 83.34},
                {"kva": 15, "base_current": 62.5, "max_short_circuit": 125.0},
                {"kva": 25, "base_current": 104.17, "max_short_circuit": 208.34},
                {"kva": 37.5, "base_current": 156.25, "max_short_circuit": 312.5},
                {"kva": 50, "base_current": 208.33, "max_short_circuit": 416.66},
                {"kva": 75, "base_current": 312.5, "max_short_circuit": 625.0},
                {"kva": 100, "base_current": 416.67, "max_short_circuit": 833.34},
                {"kva": 167, "base_current": 695.83, "max_short_circuit": 1391.66},
                {"kva": 250, "base_current": 1041.67, "max_short_circuit": 2083.34},
            ],
            "three_phase_480v": [
                {"kva": 3, "base_current": 3.6, "max_short_circuit": 7.2},
                {"kva": 6, "base_current": 7.2, "max_short_circuit": 14.4},
                {"kva": 9, "base_current": 10.8, "max_short_circuit": 21.6},
                {"kva": 15, "base_current": 18.0, "max_short_circuit": 36.0},
                {"kva": 30, "base_current": 36.1, "max_short_circuit": 72.2},
                {"kva": 45, "base_current": 54.1, "max_short_circuit": 108.2},
                {"kva": 75, "base_current": 90.2, "max_short_circuit": 180.4},
                {"kva": 112.5, "base_current": 135.3, "max_short_circuit": 270.6},
                {"kva": 150, "base_current": 180.4, "max_short_circuit": 360.8},
                {"kva": 225, "base_current": 270.6, "max_short_circuit": 541.2},
                {"kva": 300, "base_current": 360.8, "max_short_circuit": 721.6},
                {"kva": 500, "base_current": 601.4, "max_short_circuit": 1202.8},
                {"kva": 750, "base_current": 902.1, "max_short_circuit": 1804.2},
                {"kva": 1000, "base_current": 1202.8, "max_short_circuit": 2405.6},
            ],
            "distribution_11kv": [
                {"kva": 100, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 139.2, "impedance": 4.5},
                {"kva": 200, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 278.4, "impedance": 4.5},
                {"kva": 315, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 439.0, "impedance": 5.0},
                {"kva": 630, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 878.0, "impedance": 5.5},
                {"kva": 1000, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 1393.3, "impedance": 6.0},
                {"kva": 1250, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 1741.6, "impedance": 6.0},
                {"kva": 1600, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 2229.3, "impedance": 6.5},
                {"kva": 2000, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 2786.6, "impedance": 6.5},
                {"kva": 2500, "primary_voltage": 11000, "secondary_voltage": 415, "base_current": 3483.3, "impedance": 7.0},
            ],
            "power_transformers": [
                {"mva": 12.5, "voltage": "66/11 kV", "base_current_hv": 109.5, "base_current_lv": 656.0, "impedance": 8.0},
                {"mva": 20, "voltage": "66/11 kV", "base_current_hv": 175.2, "base_current_lv": 1049.7, "impedance": 8.5},
                {"mva": 31.5, "voltage": "66/11 kV", "base_current_hv": 276.0, "base_current_lv": 1653.0, "impedance": 9.0},
                {"mva": 100, "voltage": "132/11 kV", "base_current_hv": 437.6, "base_current_lv": 5247.0, "impedance": 12.0},
                {"mva": 160, "voltage": "132/11 kV", "base_current_hv": 700.2, "base_current_lv": 8395.2, "impedance": 12.5},
                {"mva": 315, "voltage": "400/220 kV", "base_current_hv": 454.7, "base_current_lv": 825.8, "impedance": 14.0},
                {"mva": 500, "voltage": "765/400 kV", "base_current_hv": 377.6, "base_current_lv": 721.7, "impedance": 15.0},
            ]
        }
    
    def init_ui(self):
        """Initialize the main UI components"""
        self.setWindowTitle('GE Transformer & Short Circuit Calculator')
        self.setMinimumSize(1200, 700)
        self.resize(1400, 800)
        self.set_dark_theme()
        self.create_menu_bar()
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        main_layout = QVBoxLayout(main_widget)
        main_layout.setSpacing(50)
        main_layout.setContentsMargins(50, 50, 50, 50)
        
        # Header section
        header_layout = self.create_header()
        main_layout.addLayout(header_layout)
        
        # Main buttons section
        buttons_layout = self.create_buttons_section()
        main_layout.addLayout(buttons_layout)
        
        # Footer
        footer_layout = self.create_footer()
        main_layout.addLayout(footer_layout)
        
        main_layout.addStretch()
    
    def create_menu_bar(self):
        """Create menu bar with about option"""
        menubar = self.menuBar()
        menubar.setStyleSheet("""
            QMenuBar {
                background-color: #1e4a73;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 8px;
            }
            QMenuBar::item {
                padding: 10px 20px;
                margin: 3px;
            }
            QMenuBar::item:selected {
                background-color: #2771b3;
                border-radius: 5px;
            }
            QMenu {
                background-color: #1e4a73;
                color: white;
                border: 2px solid #2771b3;
            }
            QMenu::item {
                padding: 10px 20px;
            }
            QMenu::item:selected {
                background-color: #2771b3;
            }
        """)
        
        # Help menu
        help_menu = menubar.addMenu('Help')
        about_action = QAction('About', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def show_about(self):
        """Show about dialog"""
        about_dialog = AboutDialog(self)
        about_dialog.exec_()
        
    def set_dark_theme(self):
        """Set the dark blue theme for the application"""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0a2543;
                color: white;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QWidget {
                background-color: #0a2543;
                color: white;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
        """)
    
    def create_header(self):
        """Create the header with GE logo and title"""
        header_layout = QVBoxLayout()
        header_layout.setSpacing(30)
        
        # Logo and title row
        title_row = QHBoxLayout()
        
        # GE Logo
        logo_label = QLabel()
        logo_label.setFixedSize(120, 120)
        logo_label.setStyleSheet("""
            QLabel {
                background-color: #1e4a73;
                border: 4px solid white;
                border-radius: 60px;
                font-size: 28px;
                font-weight: bold;
            }
        """)
        logo_label.setText("GE")
        logo_label.setAlignment(Qt.AlignCenter)
        logo_label.setFont(QFont('Segoe UI', 28, QFont.Bold))
        
        # Title section
        title_section = QVBoxLayout()
        title_section.setSpacing(10)
        
        title_label = QLabel('Transformer & Short Circuit Calculator')
        title_label.setFont(QFont('Segoe UI', 42, QFont.Bold))
        title_label.setStyleSheet("color: white; margin-left: 40px;")
        
        subtitle_label = QLabel('Professional Power System Analysis Tool')
        subtitle_label.setFont(QFont('Segoe UI', 20))
        subtitle_label.setStyleSheet("color: #b0b0b0; margin-left: 40px;")
        
        version_label = QLabel('Version 2.0 - Industry Standard Calculations')
        version_label.setFont(QFont('Segoe UI', 16))
        version_label.setStyleSheet("color: #4da6ff; margin-left: 40px;")
        
        title_section.addWidget(title_label)
        title_section.addWidget(subtitle_label)
        title_section.addWidget(version_label)
        
        title_row.addWidget(logo_label)
        title_row.addLayout(title_section)
        title_row.addStretch()
        
        header_layout.addLayout(title_row)
        
        return header_layout
    
    def create_buttons_section(self):
        """Create the main buttons section"""
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(50)
        
        # Section title
        section_title = QLabel("Select Calculation Type")
        section_title.setFont(QFont('Segoe UI', 28, QFont.Bold))
        section_title.setAlignment(Qt.AlignCenter)
        section_title.setStyleSheet("color: #4da6ff; margin: 40px 0px;")
        
        buttons_layout.addWidget(section_title)
        
        # Buttons grid
        buttons_grid = QHBoxLayout()
        buttons_grid.setSpacing(60)
        buttons_grid.setAlignment(Qt.AlignCenter)
        
        # Simple Calculations Button
        simple_button = self.create_simple_button(
            "🔌", 
            "Simple Calculations",
            self.open_simple_calculations
        )
        
        # Detailed Calculations Button
        detailed_button = self.create_simple_button(
            "⚡", 
            "Detailed Calculations",
            self.open_detailed_calculations
        )
        
        # Transformer Tables Button
        tables_button = self.create_simple_button(
            "📋", 
            "Transformer Tables",
            self.open_transformer_tables
        )
        
        buttons_grid.addWidget(simple_button)
        buttons_grid.addWidget(detailed_button)
        buttons_grid.addWidget(tables_button)
        
        buttons_layout.addLayout(buttons_grid)
        
        return buttons_layout
    
    def create_simple_button(self, icon, title, callback):
        """Create a clean, simple button"""
        button = QPushButton()
        button.setFixedSize(300, 200)
        button.setCursor(Qt.PointingHandCursor)
        
        # Create layout for button content
        button_layout = QVBoxLayout(button)
        button_layout.setSpacing(20)
        button_layout.setAlignment(Qt.AlignCenter)
        
        # Icon
        icon_label = QLabel(icon)
        icon_label.setFont(QFont('Segoe UI', 72))
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet("color: #4da6ff; background: transparent; border: none;")
        
        # Title
        title_label = QLabel(title)
        title_label.setFont(QFont('Segoe UI', 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: white; background: transparent; border: none;")
        title_label.setWordWrap(True)
        
        button_layout.addWidget(icon_label)
        button_layout.addWidget(title_label)
        
        # Button styling
        button.setStyleSheet("""
            QPushButton {
                background-color: #1e4a73;
                border: 3px solid #2771b3;
                border-radius: 25px;
                padding: 20px;
            }
            QPushButton:hover {
                background-color: #2771b3;
                border: 3px solid #4da6ff;
                transform: translateY(-5px);
            }
            QPushButton:pressed {
                background-color: #3a8bc7;
                transform: translateY(0px);
            }
        """)
        
        button.clicked.connect(callback)
        
        return button
    
    def create_footer(self):
        """Create footer with additional information"""
        footer_layout = QHBoxLayout()
        
        footer_text = QLabel("Based on IEEE/IEC Standards • Blakley Calculator Methodology • For Electrical Engineers & Power System Professionals")
        footer_text.setFont(QFont('Segoe UI', 14))
        footer_text.setAlignment(Qt.AlignCenter)
        footer_text.setStyleSheet("color: #888888; margin-top: 50px;")
        
        footer_layout.addWidget(footer_text)
        
        return footer_layout
    
    def open_simple_calculations(self):
        """Open Simple Calculations dialog"""
        dialog = SimpleCalculationDialog(self)
        dialog.exec_()
    
    def open_detailed_calculations(self):
        """Open Detailed Calculations dialog"""
        dialog = DetailedCalculationDialog(self)
        dialog.exec_()
    
    def open_transformer_tables(self):
        """Open Transformer Tables dialog"""
        dialog = TransformerTablesDialog(self.transformer_data, self)
        dialog.exec_()

def main():
    """Main function to run the application"""
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    # Set application properties
    app.setApplicationName("GE Transformer Calculator")
    app.setApplicationVersion("2.0")
    app.setOrganizationName("ROSHAN TECHNOLOGIES")
    
    window = TransformerCalculatorMainWindow()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()