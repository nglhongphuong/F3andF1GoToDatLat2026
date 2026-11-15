# Đà Lạt 3 ngày 2 đêm (03/12 – 06/12/2026)

Web timeline chuyến đi: lịch từng ngày, chi phí 1 người / cả nhóm, nút Google Map + tìm ảnh Google cho từng địa điểm, tick "Xong", link file Excel và poster.

## Sửa ngay trên web (data.txt = database mini)
- Bấm **✏️ Sửa** (nút đầu tiên trên thanh ngày) để bật chế độ chỉnh sửa, bấm **✅ Xong** để về giao diện bình thường.
- **＋ Thêm thẻ** cuối mỗi ngày, ✏️ sửa, 🗑️ xoá (bấm 2 lần), tick **Xong**: tất cả ghi vào data.txt.
- Refresh vẫn còn (bản nháp giữ trong trình duyệt). Bấm **💾 Lưu lên GitHub** để ghi thẳng vào `data.txt` trên nhánh `main`, cả nhóm cùng thấy.
- Kết nối GitHub 1 lần: mục *Dữ liệu → ⚙️ Kết nối GitHub*, dán **Fine-grained token** (chỉ repo này, quyền *Contents: Read and write*). Token chỉ lưu trong trình duyệt người nhập.
- **👥 Người tham gia**: tên, vai trò, SĐT, địa chỉ nhà. SĐT + địa chỉ được **mã hoá bằng mật khẩu nhóm** (AES-GCM) trước khi lưu, repo public cũng không đọc được nếu không có mật khẩu. Quên mật khẩu = mất phần đó.

## Sửa dữ liệu bằng tay (tên, giá, địa điểm)
Mọi thứ nằm trong **`data.txt`**, không cần đụng code:
- `[THÀNH VIÊN]`: mỗi dòng 1 tên, web tự nhân chi phí theo số người.
- `[NGÀY]`: mỗi dòng có dạng `Giờ | Địa điểm | Giá thấp/người | Giá cao/người | Ghi chú | Địa chỉ | Ảnh`
- `[QUÁN ĂN]`, `[CHI PHÍ CHUNG]`, `[LƯU Ý]`: thêm hoặc xoá dòng thoải mái.

Trên GitHub: mở `data.txt` → bấm ✏️ → sửa → **Commit changes**. Khoảng 1 phút sau web tự cập nhật.

(Tuỳ chọn) Chạy `python build.py` để nhúng data.txt vào index.html, giúp mở file offline vẫn có dữ liệu.

## Dùng trên điện thoại
Web làm theo kiểu app điện thoại: có thanh tab ở dưới (Lịch trình · Tick · Chi phí · Quán ăn · Nhạc), chọn ngày bằng các nút ở trên hoặc vuốt ngang.
Muốn có icon trên màn hình chính: iPhone mở bằng Safari → Chia sẻ → *Thêm vào MH chính*; Android mở bằng Chrome → ⋮ → *Thêm vào màn hình chính*.

## Nhạc nền
Mở web là nhạc tự phát. Nếu trình duyệt chặn tự phát (điện thoại hay chặn), web hiện màn hình chào **"Chạm để vào & bật nhạc"**, chạm 1 lần là có nhạc. Tắt tự phát: ghi `Tự phát nhạc = không` trong data.txt.

Nút 🎵 góc phải dưới. Mặc định là nhạc lofi tự tạo bằng code (bài gốc, không vướng bản quyền).
Muốn đổi bài: bỏ file `.mp3` vào thư mục `music/` rồi ghi `Nhạc = music/ten-file.mp3` trong data.txt,
hoặc dán link YouTube/Spotify (bấm nút sẽ mở link đó).

## Đưa lên GitHub Pages (miễn phí)
1. Vào github.com → **New repository** → đặt tên, ví dụ `dalat-3n2d` → chọn **Public** → Create.
2. Bấm **uploading an existing file** → kéo **toàn bộ file và thư mục** trong folder này vào (gồm cả thư mục `images/`) → Commit.
3. Vào **Settings → Pages** → Source: *Deploy from a branch* → Branch: `main` / `(root)` → Save.
4. Chờ 1–2 phút, web sẽ có ở `https://<tên-github>.github.io/dalat-3n2d/`

## Các file
| File | Nội dung |
|---|---|
| `index.html` | Trang web |
| `data.txt` | Dữ liệu chuyến đi (sửa ở đây) |
| `template.html`, `build.py` | Khuôn trang + script nhúng dữ liệu |
| `DaLat_3N2D_timeline.xlsx` | File Excel timeline |
| `poster.png` | Poster |
| `images/` | Ảnh minh hoạ |
