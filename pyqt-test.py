from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QSlider, QLabel, QPushButton, QHBoxLayout, QFormLayout, QGridLayout
from PyQt5.QtGui import QImage, QPixmap
import cv2
import sys

class MainApp(QTabWidget):

    def __init__(self):
        QTabWidget.__init__(self)
        self.acquisition_tab = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.video_size = QSize(1280, 720)
        self.addTab(self.acquisition_tab,"Acquisition")
        self.addTab(self.tab2,"Tab 2")
        self.addTab(self.tab3,"Tab 3")
        self.acquisition_tab_UI()
        self.setWindowTitle("tab demo")

    def acquisition_tab_UI(self):
        """Initialize widgets.
        """
        self.image_label = QLabel()
        self.image_label.setFixedSize(self.video_size)

        start_preview_button = QPushButton("Start preview")
        start_preview_button.clicked.connect(self.setup_camera)

        stop_preview_button = QPushButton("Stop preview")
        stop_preview_button.clicked.connect(self.stop_preview)

        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(self.close)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.saveVideo)

        brightness_label = QLabel("Brightness")
        brightness_slider = QSlider(Qt.Horizontal, self)
        brightness_slider.setFocusPolicy(Qt.NoFocus)
        brightness_slider.valueChanged[int].connect(self.changedBrightnessValue)
        brightness_slider.setMaximum(255)

        contrast_label = QLabel("Contrast")
        contrast_slider = QSlider(Qt.Horizontal, self)
        contrast_slider.setFocusPolicy(Qt.NoFocus)
        contrast_slider.valueChanged[int].connect(self.changedContrastValue)
        contrast_slider.setMaximum(255)

        saturation_label = QLabel("Saturation")
        saturation_slider = QSlider(Qt.Horizontal, self)
        saturation_slider.setFocusPolicy(Qt.NoFocus)
        saturation_slider.valueChanged[int].connect(self.changedSaturationValue)
        saturation_slider.setMaximum(255)

        l2 = QFormLayout();
        l2.addWidget(QLabel());
        l2.addWidget(QLabel());
        l2.addWidget(QLabel());
        l2.addWidget(QLabel());
        l2.addWidget(QLabel());
        l2.addRow(brightness_label, brightness_slider)
        l2.addRow(contrast_label, contrast_slider)
        l2.addRow(saturation_label, saturation_slider)

        l3 = QHBoxLayout();
        l3.addWidget(start_preview_button)
        l3.addWidget(stop_preview_button)
        l3.addWidget(save_button)
        l3.addWidget(quit_button)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.image_label, 0, 0)
        grid.addLayout(l3,1,0)

        layout = QHBoxLayout();
        layout.addLayout(grid);
        layout.addLayout(l2);
        self.acquisition_tab.setLayout(layout)

    def changedBrightnessValue(self,value):
        brightness = (value - 0)/(255 - 0)
        self.capture.set(10,brightness)

    def changedContrastValue(self,value):
        contrast = (value - 0)/(255 - 0)
        self.capture.set(11,contrast)

    def changedSaturationValue(self,value):
        saturation = (value - 0)/(255 - 0)
        self.capture.set(12,saturation)

    def setup_camera(self):
        """Initialize camera.
        """
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, self.video_size.width())
        self.capture.set(4, self.video_size.height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)

    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(image))

    def saveVideo(self):
        print("algo")

    def stop_preview(self):
        self.timer.stop();
        self.capture.release();



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainApp()
    win.show()
    sys.exit(app.exec_())
