# import sys
# import cv2
# import numpy as np
# from PyQt6.QtWidgets import (
#     QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout, QWidget, QSlider, QDialog, QFormLayout, QLineEdit, QDialogButtonBox
# )
# from PyQt6.QtGui import QPixmap, QImage
# from PyQt6.QtCore import Qt



# class ImageApp(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("تطبيق الصور والفلاتر")
#         self.setGeometry(100, 100, 800, 600)

#         # Initialize variables
#         self.image = None
#         self.modified_image = None
#         self.image_path = None

#         # Main layout
#         main_layout = QVBoxLayout()

#         # Buttons
#         button_layout = QHBoxLayout()

#         self.open_button = QPushButton("فتح صورة")
#         self.open_button.clicked.connect(self.open_image)
#         button_layout.addWidget(self.open_button)

#         self.filter_button = QPushButton("تطبيق فلتر")
#         self.filter_button.clicked.connect(self.choose_filter)
#         button_layout.addWidget(self.filter_button)

#         self.resize_button = QPushButton("تغيير الأبعاد")
#         self.resize_button.clicked.connect(self.resize_image)
#         button_layout.addWidget(self.resize_button)
        
#         self.capture_button = QPushButton("التقاط صورة")
#         self.capture_button.clicked.connect(self.capture_image)
#         button_layout.addWidget(self.capture_button)

#         self.draw_button = QPushButton("الرسم على الصورة")
#         self.draw_button.clicked.connect(self.draw_on_image)
#         button_layout.addWidget(self.draw_button)


#         self.info_button = QPushButton("معلومات الصورة")
#         self.info_button.clicked.connect(self.show_image_info)
#         button_layout.addWidget(self.info_button)




#         self.save_button = QPushButton("حفظ الصورة")
#         self.save_button.clicked.connect(self.save_image)
#         button_layout.addWidget(self.save_button)

#         main_layout.addLayout(button_layout)

#         # Image display
#         self.image_label = QLabel("لم يتم تحميل صورة")
#         self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         main_layout.addWidget(self.image_label)

#         # Main widget
#         main_widget = QWidget()
#         main_widget.setLayout(main_layout)
#         self.setCentralWidget(main_widget)

    

#     def open_image(self):
#         file_path, _ = QFileDialog.getOpenFileName(self, "فتح صورة", "", "Image Files (*.png *.jpg *.bmp)")
#         if file_path:
#             self.image = cv2.imread(file_path)
#             self.modified_image = self.image.copy()
#             self.image_path = file_path
#             self.display_image(self.image)

#     def choose_filter(self):
#         if self.image is None:
#             print("لا توجد صورة لتطبيق الفلتر.")
#             return

#         filters = {
#             "Gray": self.apply_gray_filter,
#             "Blur": self.apply_blur_filter,
#             "Edge Detection": self.apply_edge_filter,
#             "Invert": self.apply_invert_filter,
#             "Sepia": self.apply_sepia_filter,
#             "Sharpen": self.apply_sharpen_filter
#         }

#         dialog = QDialog(self)
#         dialog.setWindowTitle("اختر فلتر")
#         layout = QVBoxLayout()

#         for name, func in filters.items():
#             button = QPushButton(name)
#             button.clicked.connect(lambda _, f=func: self.apply_filter_and_close(dialog, f))
#             layout.addWidget(button)

#         dialog.setLayout(layout)
#         dialog.exec()

#     def apply_filter_and_close(self, dialog, filter_func):
#         filter_func()
#         dialog.close()

#     def apply_gray_filter(self):
#         self.modified_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
#         self.display_image(self.modified_image, is_gray=True)

#     def apply_blur_filter(self):
#         self.modified_image = cv2.GaussianBlur(self.image, (15, 15), 0)
#         self.display_image(self.modified_image)

#     def apply_edge_filter(self):
#         self.modified_image = cv2.Canny(self.image, 100, 200)
#         self.display_image(self.modified_image, is_gray=True)

#     def apply_invert_filter(self):
#         self.modified_image = cv2.bitwise_not(self.image)
#         self.display_image(self.modified_image)

#     def apply_sepia_filter(self):
#         kernel = np.array([[0.272, 0.534, 0.131],
#                            [0.349, 0.686, 0.168],
#                            [0.393, 0.769, 0.189]])
#         self.modified_image = cv2.transform(self.image, kernel)
#         self.modified_image = np.clip(self.modified_image, 0, 255).astype(np.uint8)
#         self.display_image(self.modified_image)

#     def apply_sharpen_filter(self):
#         kernel = np.array([[0, -1, 0],
#                            [-1, 5, -1],
#                            [0, -1, 0]])
#         self.modified_image = cv2.filter2D(self.image, -1, kernel)
#         self.display_image(self.modified_image)

#     def resize_image(self):
#         if self.image is None:
#             print("لا توجد صورة لتغيير أبعادها.")
#             return

#         dialog = QDialog(self)
#         dialog.setWindowTitle("تغيير أبعاد الصورة")
#         layout = QFormLayout()

#         width_input = QLineEdit()
#         height_input = QLineEdit()
#         layout.addRow("العرض (بالبكسل):", width_input)
#         layout.addRow("الارتفاع (بالبكسل):", height_input)

#         button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
#         button_box.accepted.connect(lambda: self.apply_resize(dialog, width_input, height_input))
#         button_box.rejected.connect(dialog.reject)
#         layout.addWidget(button_box)

#         dialog.setLayout(layout)
#         dialog.exec()

#     def apply_resize(self, dialog, width_input, height_input):
#         try:
#             width = int(width_input.text())
#             height = int(height_input.text())
#             self.modified_image = cv2.resize(self.image, (width, height))
#             self.display_image(self.modified_image)
#             dialog.accept()
#         except ValueError:
#             print("يرجى إدخال قيم صحيحة للأبعاد.")

#     def save_image(self):
#         if self.modified_image is None:
#             print("لا توجد صورة لحفظها.")
#             return

#         file_path, _ = QFileDialog.getSaveFileName(self, "حفظ الصورة", "", "Image Files (*.png *.jpg *.bmp)")
#         if file_path:
#             cv2.imwrite(file_path, self.modified_image)
#             print("تم حفظ الصورة بنجاح.")

#     def display_image(self, img, is_gray=False):
#         if is_gray:
#             img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
#         else:
#             img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#         h, w, ch = img.shape
#         bytes_per_line = ch * w
#         qt_img = QImage(img.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
#         pixmap = QPixmap.fromImage(qt_img)
#         self.image_label.setPixmap(pixmap)




#     def capture_image(self):
#         # الدالة الأولى: التقاط صورة من الكاميرا
#         cap = cv2.VideoCapture(0)  # فتح الكاميرا
#         if not cap.isOpened():
#             print("لا يمكن الوصول إلى الكاميرا.")
#             return
#         ret, frame = cap.read()
#         if ret:
#             self.image = frame
#             self.modified_image = frame.copy()
#             self.display_image(self.image)
#         cap.release()

#     def draw_on_image(self):
#     # الدالة الثانية: السماح بالرسم بحرية على الصورة
#      if self.image is None:
#         print("لا توجد صورة للرسم عليها.")
#         return

#      def draw(event, x, y, flags, param):
#         if event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
#             cv2.circle(self.modified_image, (x, y), 5, (0, 0, 255), -1)
#             self.display_image(self.modified_image)

#      cv2.namedWindow("رسم على الصورة")
#      cv2.setMouseCallback("رسم على الصورة", draw)
#      while True:
#         cv2.imshow("رسم على الصورة", self.modified_image)
#         if cv2.waitKey(20) & 0xFF == 27:  # الضغط على زر ESC للخروج
#             break
#      cv2.destroyAllWindows()

#     def add_shapes(self):
#     # الدالة الثالثة: نافذة اختيار الأشكال الهندسية
#      if self.image is None:
#         print("لا توجد صورة لإضافة الأشكال.")
#         return

#      dialog = QDialog(self)
#      dialog.setWindowTitle("إضافة أشكال هندسية")
#      layout = QVBoxLayout()

#     def add_shapes(self):
#     # الدالة الثالثة: نافذة اختيار الأشكال الهندسية مع سحب وإفلات
#      if self.image is None:
#         print("لا توجد صورة لإضافة الأشكال.")
#         return

#      dialog = QDialog(self)
#      dialog.setWindowTitle("إضافة أشكال هندسية")
#      layout = QVBoxLayout()

#      shapes = ["مستطيل", "دائرة", "خط", "مثلث", "أشكال متعددة", "نجمة"]

#     # تفعيل حالة السحب والإفلات
#      self.drawing_shape = None
#      self.start_pos = None

#      def on_button_click(shape_type):
#         self.drawing_shape = shape_type
#         print(f"تم اختيار الشكل: {shape_type}")

#      for shape in shapes:
#         button = QPushButton(shape)
#         button.clicked.connect(lambda _, s=shape: on_button_click(s))
#         layout.addWidget(button)

#      dialog.setLayout(layout)
#      dialog.exec()



#     def show_image_info(self):
#         # الدالة الرابعة: عرض معلومات عن الصورة
#         if self.image is None:
#             print("لا توجد صورة لعرض معلوماتها.")
#             return

#         height, width, channels = self.image.shape
#         info = f"أبعاد الصورة: {width}x{height}\nعدد القنوات: {channels}"
#         dialog = QDialog(self)
#         dialog.setWindowTitle("معلومات الصورة")
#         layout = QVBoxLayout()
#         label = QLabel(info)
#         layout.addWidget(label)
#         dialog.setLayout(layout)
#         dialog.exec()



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ImageApp()
#     window.show()
#     sys.exit(app.exec())



from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QInputDialog
from PyQt6.QtGui import QPixmap, QImage, QPainter, QPen
from PyQt6.QtCore import Qt, QPoint
from PIL import Image, ImageQt, ImageFilter
import cv2
import sys
import os

class ImageEditor(QMainWindow):
    def init(self):
        super().init()
        self.setWindowTitle("برنامج تعديل الصور")
        self.setGeometry(100, 100, 900, 700)

        # واجهة المستخدم
        self.image_label = QLabel(self)
        self.image_label.setGeometry(20, 20, 640, 480)
        self.image_label.setStyleSheet("border: 1px solid black;")
        self.image_label.setMouseTracking(True)

        self.load_button = QPushButton("إدراج صورة", self)
        self.load_button.setGeometry(700, 50, 150, 30)
        self.load_button.clicked.connect(self.load_image)

        self.filter_button = QPushButton("إضافة فلاتر", self)
        self.filter_button.setGeometry(700, 100, 150, 30)
        self.filter_button.clicked.connect(self.add_filter)

        self.resize_button = QPushButton("تغيير الأبعاد", self)
        self.resize_button.setGeometry(700, 150, 150, 30)
        self.resize_button.clicked.connect(self.resize_image)

        self.capture_button = QPushButton("التقاط صورة", self)
        self.capture_button.setGeometry(700, 200, 150, 30)
        self.capture_button.clicked.connect(self.capture_image)

        self.draw_button = QPushButton("الرسم على الصورة", self)
        self.draw_button.setGeometry(700, 250, 150, 30)
        self.draw_button.clicked.connect(self.enable_drawing)

        self.info_button = QPushButton("معلومات الصورة", self)
        self.info_button.setGeometry(700, 300, 150, 30)
        self.info_button.clicked.connect(self.show_image_info)

        self.save_button = QPushButton("حفظ الصورة", self)
        self.save_button.setGeometry(700, 350, 150, 30)
        self.save_button.clicked.connect(self.save_image)

        # المتغيرات
        self.image = None
        self.drawing = False
        self.last_point = QPoint()
        self.pixmap = None  # لتخزين نسخة من الصورة للرسم عليها

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "اختر صورة", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()

    def add_filter(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.BLUR)
            self.display_image()

    def resize_image(self):
        if self.image:
            width, ok1 = QInputDialog.getInt(self, "تغيير العرض", "أدخل العرض الجديد:")
            height, ok2 = QInputDialog.getInt(self, "تغيير الطول", "أدخل الطول الجديد:")
            if ok1 and ok2:
                self.image = self.image.resize((width, height))
                self.display_image()

    def capture_image(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if ret:
            image_path = "captured_image.jpg"
            cv2.imwrite(image_path, frame)
            self.image = Image.open(image_path)
            self.display_image()

    def enable_drawing(self):
        if self.image:
            self.drawing = True
            self.pixmap = self.image_label.pixmap().copy()  # نسخة للرسم عليها

    def mousePressEvent(self, event):
        if self.drawing:
            self.last_point = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if self.drawing and event.buttons() == Qt.MouseButton.LeftButton:
            painter = QPainter(self.pixmap)
            pen = QPen(Qt.GlobalColor.black, 3, Qt.PenStyle.SolidLine)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.position().toPoint())
            painter.end()
            self.last_point = event.position().toPoint()
            self.image_label.setPixmap(self.pixmap)  # تحديث QLabel

    def mouseReleaseEvent(self, event):
        if self.drawing:
            self.drawing = False