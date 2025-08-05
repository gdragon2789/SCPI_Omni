import os
import sys

# Lấy thư mục hiện tại của file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Lên 2 cấp để đến thư mục SCPI_Omni
parent_dir = os.path.abspath(os.path.join(current_dir,".." ,".."))
# Thêm vào sys.path nếu chưa có
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from api.__init__ import *
