
Anh
Việt
=========================
🤖 ChatGPT Discord Bot
=========================

📄 ABOUT:
This is a Discord chatbot written in Python that uses the OpenRouter API to generate AI responses.
It works only in the channel where it's set up using the `cdvsetup` command.

✅ Features:
- User specific memory
- Typing indicator
- Channel lock/unlock setup
- Simple prefix commands

=========================
📁 PROJECT FILES:
=========================

1. bot.py           → Main Python script that runs the bot.
2. config.json      → Configuration file (API key, model, and settings).
3. requirements.txt → Python dependencies for Katabump or local hosting.

=========================
⚙️ SETUP INSTRUCTIONS:
=========================

🔸 STEP 1: Edit `config.json`

# Open the `config.json` file and update the following:
- `"api_key"`: Replace with your OpenRouter API key (line 2)
- `"system_context"`: Customize the assistant personality (line 4)
- `"error_message"`: Change the fallback message shown on error (line 5)

🔸 STEP 2: Edit `bot.py`
- At the bottom, replace `<YOUR_BOT_TOKEN>` with your Bot Token.

🔻 STATUS : (bot.py line 35-36) 
- status=discord.Status.online # Options: online, idle, dnd, invisible
- activity=discord...., name="<YOUR_STATUS_MESSAGE>"), #enjoyy!!!
1.275
=========================
🤖 ChatGPT Discord Bot
=========================

📄 GIỚI THIỆU:
Đây là một chatbot Discord được viết bằng Python, sử dụng API OpenRouter để tạo ra các phản hồi AI.

Nó chỉ hoạt động trong kênh được thiết lập bằng lệnh `cdvsetup`.

✅ Tính năng:
- Bộ nhớ dành riêng cho người dùng
- Chỉ báo đang gõ
- Thiết lập khóa/mở khóa kênh
- Các lệnh tiền tố đơn giản

=========================
📁 TỆP DỰ ÁN:

=========================

1. bot.py → Tập lệnh Python chính chạy bot.
2. config.json → Tệp cấu hình (khóa API, mô hình và cài đặt).

3. requirements.txt → Các thư viện Python cần thiết cho Katabump hoặc hosting cục bộ.

=========================
⚙️ HƯỚNG DẪN THIẾT LẬP:
=========================

🔸 BƯỚC 1: Chỉnh sửa `config.json`

# Mở tệp `config.json` và cập nhật những mục sau:

- `"api_key"`: Thay thế bằng khóa API OpenRouter của bạn (dòng 2)

- `"system_context"`: Tùy chỉnh tính cách của trợ lý ảo (dòng 4)

- `"error_message"`: Thay đổi thông báo lỗi hiển thị khi xảy ra lỗi (dòng 5)

🔸 BƯỚC 2: Chỉnh sửa `bot.py`
- Ở cuối tệp, thay thế `<YOUR_BOT_TOKEN>` bằng Mã thông báo Bot của bạn.

🔻 TRẠNG THÁI : (bot.py dòng 35-36)
- status=discord.Status.online # Tùy chọn: online, idle, dnd, invisible
- activity=discord...., name="<THÔNG BÁO TRẠNG THÁI CỦA BẠN>"), #Chúc vui vẻ!!!
Gửi ý kiến phản hồi
