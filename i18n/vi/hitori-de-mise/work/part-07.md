- Nó mô phỏng thời điểm thanh toán được chia thành "ngày 10" và "ngày 25 / cuối tháng".

- Dữ liệu được lưu trong trình duyệt (bộ nhớ đệm).

Chỉ vậy thôi đã đủ tiện, nhưng tôi lại tham lam. "Tôi muốn dữ liệu vẫn còn khi đóng trình duyệt. Tôi cũng muốn kiểm tra trên điện thoại."

#### Giai đoạn 2: Làm quen với một công cụ lạ, "Firebase"

Tôi từng nghĩ đến việc liên kết với một bảng tính, nhưng gợi ý của Gemini lại nằm ngoài dự đoán.

"Nếu xét đến tính thời gian thực và hiệu quả, hãy dùng 'Firebase' của Google. Gói miễn phí là đủ để vận hành."

"Firebase...?" Tôi chưa bao giờ nghe đến từ này. Nhưng với trực giác từ những ngày làm điều phối hệ thống, tôi quyết định: "AI đã khuyên mạnh như vậy thì cứ theo."

Kết quả là nhờ dùng một cơ sở dữ liệu tên là Firestore, dữ liệu được lưu giữ an toàn trên đám mây.

#### Giai đoạn 3: Đăng nhập Google và hệ thống phê duyệt

Đây là chuyện tiền bạc, nên để ai cũng xem được thì không ổn.

Lúc đầu tôi nghĩ đến thứ gì đó như một "cụm mật khẩu", nhưng Gemini gợi ý: "Nếu muốn bảo mật mạnh hơn, hãy dùng đăng nhập Google."

Rồi khi tôi nói: "Tôi muốn chỉ những nhân viên do tôi duyệt mới xem được", nó thậm chí còn xây dựng "một hệ thống để quản trị viên phê duyệt và xóa thành viên ngay trên màn hình".

### 6-3. Giai đoạn 4-5: Đối mặt với màn hình đen (terminal)

Từ đây là rào cản lớn nhất của vibe coding: đưa ứng dụng lên internet (deploy).

#### Cảnh báo: Từ đây trở đi là khóa "Đai đen"

Vài trang tiếp theo là phần "thực hành" khó nhất của cuốn sách này. Bạn sẽ thao tác trên một "màn hình đen (terminal)" như những gì hacker dùng trong phim.

Tôi xin nói thật. Chắc chắn bạn sẽ gặp lỗi ở đây. Tôi cũng vậy. Bạn sẽ đụng phải những bức tường như "lỗi quyền hạn của PowerShell", đọc lên như thần chú. Nhưng đừng sợ. Việc bạn làm ở đây vẫn như cũ: chỉ cần "chụp màn hình báo lỗi rồi ném cho AI".

Sự thật tôi học được trong những ngày làm nghề hệ thống là thế này: "Ngay cả dân chuyên nghiệp cũng gặp lỗi. Điểm khác biệt duy nhất là khi lỗi xuất hiện thì bạn bỏ cuộc, hay đi tìm (hỏi) sự giúp đỡ." Nếu thấy quá khó, hãy bỏ qua phần này và chỉ mang theo một khả năng: "Với AI, bạn có thể làm được đến mức này."

Gemini nói:

"Chúng ta sẽ thiết lập môi trường phát triển trên máy tính Windows của bạn. Hãy cài 'Node.js' và gõ các lệnh sau trong 'VS Code'."

Tôi mở màn hình đen (terminal) theo hướng dẫn, và lập tức gặp lỗi.

"Không thể chạy do các hạn chế bảo mật của PowerShell."

Một chủ quán bình thường sẽ nản lòng ở đây.

Nhưng tôi sao chép màn hình báo lỗi rồi ném cho AI.

AI trả lời ngay: "Hãy gỡ hạn chế bằng một lệnh gọi là 'Set-ExecutionPolicy'."

Không hiểu nó có nghĩa gì, tôi vẫn gõ lệnh vào, rồi npm run build, firebase deploy...

Mỗi lần tôi gõ những ký tự như thần chú đó, chữ chạy dọc màn hình và tiến trình cứ thế tiến lên.

Và cuối cùng, ứng dụng của tôi đã xuất hiện trên web.

#### Giai đoạn 5: Biến nó thành ứng dụng điện thoại (PWA)

Ứng dụng được đăng tải lúc đầu ở trạng thái "mặt mộc" với thiết kế bị vỡ, nhưng điều này cũng được giải quyết bằng cách thêm một thiết lập gọi là "Tailwind CSS".

Rồi khi tôi hỏi: "Tôi muốn đặt biểu tượng lên màn hình chính của điện thoại và dùng như một ứng dụng", nó chỉ cho tôi các thiết lập để biến nó thành "PWA (Progressive Web App)".

Và thế là một ứng dụng riêng do tôi làm ra (mà không viết một dòng mã nào) đã ra đời ngay trong điện thoại của tôi.

![Màn hình của ứng dụng quản lý dòng tiền đã hoàn thành](images/fig-26.png)

### 6-4. Giai đoạn 6: Vấn đề sau 30 ngày và cách khắc phục

Khoảng một tháng sau khi tôi bắt đầu dùng, một vấn đề xảy ra.

"Hôm qua còn chạy được, thế mà đột nhiên không truy cập được!"

Tôi hoảng hốt hỏi Gemini, và nguyên nhân nằm ở một chỗ không ngờ tới.

"Thiết lập của cơ sở dữ liệu (Firestore) vẫn đang ở 'chế độ thử nghiệm (giới hạn 30 ngày)'. Nó đã hết hạn."

Để đỡ phải cấu hình rắc rối lúc bắt đầu phát triển, AI đã cố ý đặt một quy tắc có thời hạn.

"Hãy viết lại các quy tắc bảo mật để 'bất kỳ người dùng nào đã đăng nhập đều có thể tiếp tục sử dụng'."

Khi tôi viết lại vài dòng trong tệp thiết lập theo hướng dẫn của AI, ứng dụng đã trở lại an toàn.

Sự cố này cũng là một trải nghiệm tốt với tôi.

Tôi học được rằng "hệ thống là một thực thể sống và cần được bảo trì".

Và tôi có thêm sự yên tâm rằng "dù có sự cố xảy ra, chỉ cần hỏi AI thì luôn có lời giải".

### 6-5. Nghiên cứu tình huống 2: "Dự án nhận diện khuôn mặt" bắt đầu từ một video demo trên X (trước đây là Twitter)

Đây là một hệ thống nữa mà tôi đã đảm nhận, và là hệ thống lớn nhất.

Đó là "một hệ thống nhận diện khách bước vào qua camera, và lặng lẽ cho tôi biết tên, dữ liệu và sở thích của họ".

Nó bắt đầu từ mạng xã hội X, nơi tôi đang lướt xem một cách tình cờ.

Một video demo do một kỹ sư đăng hiện lên trên bảng tin của tôi: dùng AI tích hợp sẵn trong Google Chrome (Built-in AI) để giải thích theo thời gian thực những gì webcam đang nhìn thấy.

Bản năng của một người từng làm hệ thống trỗi dậy trong tôi.

"Đây là 'đa phương thức'. Và nếu nó được tích hợp sẵn trong trình duyệt, chẳng lẽ không thể chạy hoàn toàn trên máy tính của mình mà không phải trả tiền cho đám mây sao?"

Nếu việc này thành công, có lẽ tôi sẽ xây được một hệ thống đón tiếp khách dành riêng cho quán mà không cần cài đặt một hệ thống đắt tiền.

Tôi sao chép URL rồi ném cho Gemini.

"Tôi muốn làm điều tương tự như thế này. Hãy chỉ cho tôi cách triển khai."

#### Giai đoạn 1: Chạy được, nhưng không biết "ai" là ai

Tôi thay đổi các thiết lập (flag) của Chrome theo hướng dẫn của Gemini và dán mã vào, thế là hệ thống giống hệt bản demo chạy trơn tru.

Khi tôi xuất hiện trước camera, màn hình hiển thị dòng này:

"Một người đeo kính đang ngồi trước máy tính."

Nó dùng một AI tích hợp trong trình duyệt tên là GeminiNano. Ưu điểm là nó hoạt động hoàn toàn bên trong trình duyệt mà không cần kết nối đám mây, nhưng nó chỉ nhận ra được những thứ chung chung như "kính" và "người". Nó không đi xa đến mức xác định người đó là ai.

Đó là một công nghệ tuyệt vời. Nhưng với tư cách chủ nhà hàng, tôi thất vọng ngay.

"Thế này thì không được."

Điều tôi muốn biết không phải là một đặc điểm chung chung như "người đeo kính", mà là nhận dạng từng cá nhân: "Đây là khách A hay khách B?"

#### Giai đoạn 2: Rào cản tích hợp Google Photos và câu trả lời của AI

Thế là tôi đưa một ý tưởng ngây thơ cho Gemini.

"Hãy kết nối hệ thống này với Google Photos của tôi. Trong đó có dữ liệu nhóm khuôn mặt của bạn bè và khách quen của tôi, nên nếu đối chiếu với đó thì sẽ biết được tên, đúng không?"

Câu trả lời của Gemini lạnh lùng, nhưng chính xác.

"Tôi xin lỗi, nhưng điều đó là không thể. Dữ liệu nhận diện khuôn mặt trong Google Photos là thông tin riêng tư rất nhạy cảm, và vì lý do bảo mật nên không được phép dùng bởi các chương trình bên ngoài."

Cũng phải thôi. Con đường dường như dừng lại ở đây.

Nhưng từ đây mới là bản chất thực sự của "vibe coding (phát triển thông qua đối thoại)". AI không chỉ từ chối.

#### Giai đoạn 3: Một giải pháp thay thế và bước chuyển hướng

Gemini tiếp tục gợi ý thế này:

"Chúng ta không thể dùng Google Photos, nhưng có thể tự xây một hệ thống nhận diện khuôn mặt trong môi trường cục bộ bằng các thư viện mã nguồn mở (như OpenCV hay face_recognition). Chúng ta thử nhé?"

Tôi trả lời "Có" ngay lập tức.

Từ đây, kế hoạch phát triển thay đổi hoàn toàn. Thay vì dùng các tính năng của Chrome, tôi sẽ xây một hệ thống nhận diện khuôn mặt từ đầu bằng một ngôn ngữ lập trình tên là Python.

#### Giai đoạn 4: Vật lộn với màn hình đen và kết nối với bảng tính

Việc tôi phải làm không thay đổi. Tôi hỏi Gemini "cách cài các thư viện cần thiết" và dán câu trả lời vào màn hình đen (command prompt).

Khi có lỗi xuất hiện, tôi ném nguyên dòng chữ đỏ ấy trở lại cho Gemini.

Vài giờ sau, hệ thống cuối cùng đã hoàn tất.

1.  Webcam ghi lại khuôn mặt tôi.

2.  Nó đối chiếu với "dữ liệu ảnh khuôn mặt" trong một thư mục trên máy tính.

3.  Khi tìm thấy kết quả khớp, nó tra cứu danh sách khách hàng trong một Google Spreadsheet.

4.  Màn hình hiển thị "Bonta: còn lại chai vuông ○○ g."

![Hệ thống nhận diện khuôn mặt đang chạy. Nó nhận ra khuôn mặt của chủ quán và hiển thị thông tin. Hình chụp đã được làm mờ bằng mosaic bằng Gemini](images/fig-27.png)

Chi phí thuê ngoài: ¥0 (khoảng $0,00). Công sức viết mã của chính tôi: không.

Đó là khoảnh khắc một "hệ thống CRM nhận diện khuôn mặt" độc nhất vô nhị ra đời ở một góc Higashi-Nakano.

#### Giai đoạn 5: Rồi tôi nhận ra "trách nhiệm phải bảo vệ"

Hệ thống đã hoàn thành. Nhưng cùng với niềm vui, tôi cảm thấy một cơn ớn lạnh chạy dọc sống lưng.

"Khoan đã. Hiện giờ chiếc máy tính này đang giữ dữ liệu khuôn mặt (thông tin sinh trắc học) của khách, đúng không...?"

Cho đến lúc đó tôi vẫn nghĩ "miễn là chạy được thì ổn". Nhưng một khi đưa vào vận hành thực tế thì lại là chuyện khác.

Nếu máy tính này bị nhiễm virus thì sao? Dữ liệu khuôn mặt của khách và thông tin sở thích của họ (thông tin cá nhân) có thể bị rò rỉ cùng lúc.

Một chiếc máy tính độc lập không kết nối internet thì sẽ an toàn, nhưng chừng nào tôi còn xử lý đặt chỗ và mạng xã hội thì kết nối internet là thiết yếu.

"Có thể xây dựng một công cụ hữu ích" và "có thể quản lý nó một cách an toàn" là hai chuyện riêng biệt.

Chính tại đây, lần đầu tiên tôi thực sự cảm nhận được tầm quan trọng của "bảo hiểm rủi ro mạng" mà một nhân viên bảo hiểm từng nói với tôi khi đến chào mời trước đây.

Tôi đã cười: "Quán nhỏ như bọn tôi thì làm gì có tấn công mạng", nhưng giờ khi AI cho phép chúng ta xây những hệ thống tiên tiến, những chủ quán cá nhân như chúng ta cũng gánh thêm trách nhiệm của một "người quản lý dữ liệu" đúng nghĩa.

Với AI, bạn có thể có được những công cụ kỳ diệu.

