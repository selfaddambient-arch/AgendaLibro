Những điều có cảm giác là đang hiệu quả, nhưng tôi không thể chứng minh quan hệ nhân quả. Rằng nhiều khách đến theo nhóm hơn nhờ giảm giá nhóm. Rằng suất dành cho khách lần đầu/khách quay lại đang được chọn. Rằng chủ đề trong email xác nhận đã trở thành một phần của câu chuyện ở quầy. Tôi cảm nhận được điều đó ngay tại quán, nhưng tôi không thể nói "nếu không có hệ thống ấy thì họ đã không đến."

Những gì đã xây xong, nhưng tôi vẫn chưa biết hiệu quả. Giảm giá đặt sớm sẽ mang thêm bao nhiêu lượt đặt trước. Sẽ có thực sự bao nhiêu lượt đặt chỗ đến từ MCP. Tôi mới chỉ bắt đầu đo bằng báo cáo hằng tuần, và các con số sẽ có sau.

Hãy nhìn riêng sự kinh ngạc "chúng ta có thể xây được chừng này bằng AI" và kết quả "điều đó đã thay đổi việc kinh doanh ra sao". Nếu không phân biệt như vậy, chính việc xây dựng sẽ trở thành mục tiêu. Có lần chính tôi suýt rơi vào đó (như tôi đã viết ở mục 1-7).

Câu chuyện về những gì đứng sau hệ thống đặt chỗ này, tức là công nghệ, tiếp tục ở Chương 2. Nếu bạn không quan tâm đến công nghệ, hãy nhảy sang Chương 3. Ở đó tôi kể về việc những công cụ nhỏ sinh ra xung quanh hệ thống đặt chỗ này đang được chia sẻ cho cả các quán khác như thế nào.

## Chương 2: Công nghệ - phía sau hệ thống đặt chỗ

Những điểm chính của chương này

- Chất lượng các cuộc trò chuyện của AI được quyết định không phải bởi sự thông minh của AI, mà bởi "những thông tin thực tế về quán mà chúng ta trao cho nó" và "việc có một chương trình tự ý ghi đè câu trả lời của AI hay không"
- Hệ thống đặt chỗ tôi xây theo cảm giác vẫn còn một lỗ hổng cho phép thông tin cá nhân của khách bị đọc từ bên ngoài, và không có bài kiểm thử tự động nào. Tôi nhờ AI kiểm tra để tìm ra những điều này, và nhờ AI sửa
- Từ sự nhìn lại đó, tôi thay đổi cách xây dựng: xác định yêu cầu thật chi tiết trước khi xây, và trao cho AI chính bản đặc tả để nó triển khai

(Chương này có nhiều thuật ngữ kỹ thuật. Nếu bạn không quan tâm đến công nghệ, bạn có thể nhảy sang Chương 3 và câu chuyện vẫn liền mạch.)

### 2-1 Máy chủ MCP hoạt động như thế nào

MCP (Model Context Protocol) là một bộ quy ước chung để AI dùng các công cụ và dữ liệu bên ngoài. Do Anthropic đề xuất, hiện nay nó được nhiều AI hỗ trợ, trong đó có ChatGPT và Claude.

Ví von một chút, MCP là một chuẩn ổ cắm điện dành cho AI. Vì hình dạng ổ cắm được cố định, thiết bị của hãng nào cắm vào cũng chạy. Tương tự, nếu bạn dựng một khung phù hợp với hình dạng của MCP, AI nào cũng dùng được khung đó.

Một máy chủ MCP cho AI biết "bạn có thể làm gì qua khung này". Chẳng hạn máy chủ MCP của Tamuro xếp ra các công cụ như sau.

- Đọc thông tin của quán (giờ mở cửa, số chỗ ngồi, quy tắc của quán, bầu không khí)
- Đọc các suất ăn và mức giá (kết quả tính giảm giá theo số người và ngày)
- Đọc các khung giờ trống (những giờ còn đặt được trong một ngày chỉ định)
- Tạo URL của một trang đặt chỗ với các điều kiện đã điền sẵn

Khi một khách hỏi AI của chính họ: "Tối nay Tamuro còn chỗ không?", AI kết nối với máy chủ MCP của Tamuro, chọn "đọc các khung giờ trống" trong số các công cụ được xếp ra, rồi gọi nó. Máy chủ của Tamuro trả về kết quả, và AI diễn đạt thành lời cho khách.

Điều quan trọng là AI không tự xác nhận đặt chỗ. Ở phiên bản đầu, tôi cố ý để việc xác nhận đặt chỗ ra ngoài các công cụ. Tất cả những gì AI làm được là đọc, và dẫn người ta đến một trang đặt chỗ với các điều kiện đã điền sẵn. Nút xác nhận do chính khách bấm trên trang của Tamuro. Nguy cơ AI tạo ra hàng loạt lượt đặt chỗ nhầm hoặc đặt chơi được tránh ngay từ thiết kế.

Việc tính giá dùng cùng một cơ chế tính toán với trang đặt chỗ. Giá hiển thị trên biểu mẫu đặt chỗ, trong khung trò chuyện và qua MCP đều ra từ cùng một chương trình duy nhất. Đây là một ý nghĩa khác của công việc tôi sẽ viết sau, "gom việc tính giảm giá về một chỗ".

【Hình 2-1】Từ AI của khách đến trang đặt chỗ của Tamuro. Khách bấm nút xác nhận

### 2-2 Khung trò chuyện "T-AI-MURO" hoạt động như thế nào

#### Giá từ chương trình, lời từ AI

T-AI-MURO chia vai trò làm hai. Chương trình đưa ra giá và khung giờ trống bằng các phép tính cố định, còn AI diễn đạt chúng thành lời cho khách.

AI giỏi tạo văn bản, nhưng không có gì đảm bảo nó tính đúng mọi lần. Cách các mức giảm giá cộng dồn, các bậc theo số người, số ngày của giảm giá đặt sớm, có kết hợp được với Happy Hour hay không. Nếu bạn giao tất cả các quy tắc này cho AI, thế nào nó cũng sai ở đâu đó. Và một sai sót về giá làm tổn hại lòng tin của khách hơn hết.

Vì vậy, những phần không được sai thì giao cho chương trình, còn những phần truyền đạt một cách mềm mại thì giao cho AI. Cách phân chia này là nguyên tắc đầu tiên khi xây khung trò chuyện.

#### Với một quán nhỏ, bạn không cần RAG

Để AI trả lời về quán, bạn cần trao kiến thức của quán cho AI. Một phương pháp thường dùng là RAG (retrieval-augmented generation, tạo sinh tăng cường truy xuất). Bạn cắt kiến thức thành các mẩu nhỏ rồi lưu lại, và mỗi khi có câu hỏi đến, bạn chỉ tìm những phần có vẻ liên quan rồi trao cho AI. Khi kiến thức đồ sộ, phương pháp này là không thể thiếu.

Nhưng kiến thức của Tamuro không lớn đến thế. Lịch sử của quán, món ăn, các quy tắc, bầu không khí, suy nghĩ của chủ quán. Gộp tất cả lại, nó vẫn nằm gọn trong lượng AI có thể đọc cùng một lúc.

Vì vậy ở Tamuro tôi chọn để AI đọc toàn bộ văn bản kiến thức của quán mỗi lần. Không cần xây cơ chế tìm kiếm như RAG đòi hỏi, và không có gì bị sót khi tìm. Lúc đầu tôi định tái sử dụng một cơ chế RAG, nhưng giữa chừng đã chuyển sang cách đọc toàn văn.

Cho nó đọc toàn văn mỗi lần thì phí AI tốn hơn. Vì vậy tôi dùng một cơ chế tái sử dụng cùng một đoạn văn để giảm chi phí đầu vào (lưu đệm lời dẫn, prompt caching: thay vì bắt AI đọc lại cùng một đoạn mở đầu mỗi lần, nó nhớ những gì đã đọc). Chỉ cần đưa RAG vào khi kiến thức lớn lên.

#### Một chương trình tự ý ghi đè câu trả lời

Ở Chương 1, tôi đã viết rằng chỉ 9 trong 36 kịch bản đạt ở lần kiểm thử đầu. Một phần nguyên nhân nằm ở cách chương trình được dựng.

Khi điều tra, tôi tìm thấy một cơ chế còn sót lại trong đó chương trình đánh giá câu trả lời AI đã tạo ra theo từ khóa và thay nó bằng một câu cố định. Khi xuất hiện các từ như "đặt chỗ" hay "hôm nay", nó vứt câu trả lời của AI đi và thay vào một danh sách khung giờ trống. Ngay cả khi AI trả lời đúng, câu trả lời cũng không bao giờ đến được tay khách.

Hơn nữa, tôi phát hiện phần chính của kiến thức về quán (33 mục) không được đưa vào chỉ dẫn cho AI. AI đã trả lời mà không biết gì về quán.

Chất lượng các cuộc trò chuyện của AI được quyết định không phải bởi sự thông minh của chính AI, mà bởi những thông tin thực tế về quán được trao cho nó và bởi việc có một chương trình tự ý ghi đè câu trả lời của AI hay không.

#### Lấp đầy các cặp hỏi đáp dự kiến bằng cách đếm

Tôi tăng các kịch bản kiểm thử từ 36 ban đầu lên 110, rồi lên 355. Nhưng nếu người ta thêm kịch bản theo ý thích, không có cách nào biết có thiếu gì hay không. Với câu hỏi "Thế này đã đầy đủ chưa?", câu trả lời trung thực là "Chưa."

Vì vậy thay vì mở rộng phạm vi bằng trí tưởng tượng, tôi biến nó thành chuyện để máy đếm những chỗ chưa được đi qua và lấp chúng. Với bốn thứ: 33 mục kiến thức về quán, các bước chuyển giữa những lựa chọn, các bậc của giảm giá, và các tổ hợp giữa khung giờ và ngày trong tuần. Tôi đếm mỗi thứ được đi qua bao nhiêu lần trong kiểm thử, và tự động thêm kịch bản ở những chỗ số đếm bằng không.

Tôi cũng dùng một phương pháp bắt chéo sáu trục (số người, mục đích, cách uống, ngày giờ, cách diễn đạt, thực đơn) và tạo kịch bản sao cho mọi tổ hợp của hai yếu tố bất kỳ đều được đi qua ít nhất một lần.

Tôi cũng tìm thấy một lỗ hổng xoay quanh thời gian. "Hôm nay" và "từ bây giờ" được xác định theo thời gian thực lúc chạy kiểm thử, nên kết quả khi chạy vào buổi trưa và khi chạy vào ban đêm khác nhau. Vì vậy tôi cố định đồng hồ trong lúc kiểm thử và cho chạy ở năm thời điểm: trước giờ mở cửa, trong giờ kinh doanh, ngay trước giờ đóng cửa, vào ngày nghỉ thường lệ, và vào ngày lễ.

Câu trả lời của AI biến đổi đôi chút mỗi lần, ngay cả với cùng một câu hỏi. Với các kịch bản gắn trực tiếp với doanh thu, tôi đặt điều kiện là phải đạt cả ba lần khi chạy ba lần.

#### Khi ra một con số tệ, hãy nghi ngờ bài kiểm thử trước

Trong bài kiểm thử chạy 355 kịch bản ở 5 thời điểm, trong 1.775 cuộc trò chuyện, 28,5% đạt.

Thay vì bắt tay sửa ngay, trước hết tôi tách bạch: "Con số này thật sự là điểm yếu của T-AI-MURO, hay bài kiểm thử sai?" Nếu bạn sửa trong lúc bài kiểm thử sai, bạn sẽ "sửa" cả những câu trả lời đúng.

| Nguyên nhân của lỗi | Số lượng |
| --- | --- |
| Một câu cố định chặn mất câu hỏi | 276 |
| Không trả lời câu hỏi, chuyển sang quy trình đặt chỗ hoặc lời gợi ý | 266 |
| Lỗi môi trường kiểm thử (T-AI-MURO không tạo được câu trả lời vì trần chi phí) | 211 |
| Lỗi về ngày, thứ trong tuần, ngày lễ, ngày nghỉ | 142 |
| Bịa đặt hoặc khẳng định những thông tin quán không có, hứa chuyển lời nhắn | 119 |

Hai nguyên nhân đứng đầu có chung một gốc: "phản ứng với từ ngữ và thực hiện một thao tác cố định trước khi trả lời câu hỏi của khách." 211 lỗi ở vị trí thứ ba không phải lỗi của T-AI-MURO. Trần chi phí đã chạm tới giữa chừng bài kiểm thử, và T-AI-MURO đơn giản là không tạo được câu trả lời. Loại những lỗi này ra, tỷ lệ đạt trở thành 32,4%.

AI chấm cũng có thể mắc sai sót. Khi tôi rút ra 20 trường hợp và kiểm tra, có 2 lỗi nằm ở phía bài kiểm thử. Trong một trường hợp, AI chấm không biết rằng "trang đặt chỗ này có đăng ký hội viên." Người chấm cũng không biết gì ngoài các tài liệu được trao. Độ chính xác của bài kiểm thử được quyết định bởi mức đầy đủ của các quy tắc của quán trao cho AI chấm.

Trong lần kiểm thử lại sau khi sửa, tỷ lệ đạt của phần hướng dẫn về giá và suất ăn tăng từ 29,4% lên 42,7%. Tôi vẫn chưa chạy bài kiểm thử cuối cùng để duyệt lại toàn bộ các trường hợp. Để giữ chi phí thấp, tôi đã quyết định bài kiểm thử toàn bộ trường hợp chỉ chạy một lần, trước khi đưa một thay đổi lớn vào hoạt động thật. Tỷ lệ đạt vẫn đang được nâng lên ngay cả khi tôi viết cuốn sách này.

#### Bài kiểm thử đã làm dừng hoạt động thật

Kiểm thử bằng AI tốn tiền. Bài kiểm thử 36 kịch bản đầu tiên tốn khoảng ¥426 (khoảng $2,8). Phần lớn tiền dành cho "nỗ lực suy nghĩ" của AI đóng vai khách, và khi tôi tắt nó đi, 3 kịch bản tốn khoảng ¥6 (khoảng $0,04).

Nhưng rồi một ngày, giữa chừng một bài kiểm thử, số dư sử dụng AI cạn và mọi thứ dừng lại. Chỉ trong một ngày tôi đã dùng khoảng 35 triệu token (đơn vị văn bản mà AI đọc và viết). Nguyên nhân là chạy đi chạy lại bài kiểm thử 221 kịch bản, và chạy các kịch bản gắn trực tiếp với doanh thu mỗi cái bốn lần.

Điều đáng sợ là bài kiểm thử và hoạt động thật dùng chung một chiếc ví. Khi số dư hết, ngay cả khung trò chuyện đang hoạt động thật cũng dừng. Vào một ngày khác, lần này tôi chạm mức trần hằng tháng do chính tôi đặt ra, và khung trò chuyện đang hoạt động thật cùng với AI tạo chủ đề trò chuyện cho khách trong quán dừng cùng một lúc.

Mối nguy thật sự của ngân sách kiểm thử không phải hóa đơn, mà là việc hoạt động thật dùng chung chiếc ví đó.

Từ đó các quy tắc thay đổi. Làm trước những kiểm tra không tốn tiền (kiểm thử chương trình và kiểm tra màn hình tự động). Giới hạn các bài kiểm thử gọi AI ở những bài liên quan đến phần đã sửa. Chỉ chạy bài kiểm thử toàn bộ trường hợp một lần, trước khi đưa vào hoạt động thật. Ghi chi phí ước tính và một mức trần vào chỉ dẫn, và dừng lại nếu có vẻ sắp chạm. Để giữ lại tiền cho hoạt động thật, dừng kiểm thử khi mức sử dụng của cả tổ chức tiến gần mức trần.

Cũng có một bài học về cách chi phí phình ra. Có lần, chi phí của AI chấm lên tới 2,6 lần so với ước tính. Nguyên nhân là đoạn mở đầu dài trao cho AI chấm mỗi lần (kiến thức và quy tắc của quán) không được tái sử dụng, nên mỗi lần đều phát sinh một khoản phí ghi lại. Khi tôi sửa để ghi đoạn mở đầu vào một lần rồi tái sử dụng, chi phí mỗi cuộc trò chuyện giảm còn khoảng một phần ba. Chi phí AI phình ra không phải theo số lần bạn gọi nó, mà theo số lần bạn ghi lại cùng một đoạn mở đầu.

Chi phí của cùng bài kiểm thử đầy đủ 221 kịch bản đó đã giảm từ khoảng ¥1.040 (khoảng $6,9) xuống khoảng ¥400 (khoảng $2,7) nhờ các cải tiến lặp đi lặp lại. Tôi thay AI đóng vai khách bằng một kịch bản cố định, và chia thông tin trao cho AI thành một "phần lõi gửi mỗi lần" và các "mục chỉ đọc khi cần".

Vì ràng buộc về ngân sách, thiết kế đã đổi hướng theo cách tăng những phần có thể kiểm tra với chi phí bằng không, tức là những phần do chương trình quyết định. Kết quả là độ chính xác cũng tăng. Tiền làm thay đổi thiết kế.

【Hình 2-2】Kết quả các bài kiểm thử AI. Tỷ lệ đạt và phân tích các nguyên nhân gây lỗi

### 2-3 Nhờ AI kiểm tra những gì tôi đã xây

#### Tên khách có thể bị đọc từ bên ngoài

Vào tháng 8 năm 2026, khi đang xem lại cách hệ thống đặt chỗ hoạt động, tôi có một phát hiện khiến sống lưng lạnh toát.

Dữ liệu đặt chỗ của khách có thể bị bất kỳ ai đọc từ bên ngoài. Tên, số điện thoại, địa chỉ email, ô yêu cầu. Toàn bộ dữ liệu được nhập trong tất cả các lượt đặt chỗ đều có thể bị lấy ra, mà không cần xác thực.

Có một điều tôi nên nói thật. Đúng là dữ liệu có thể bị đọc từ bên ngoài. Vào thời điểm đó, trang đặt chỗ có lượng truy cập rất ít, và tôi tin rằng khó có ai thực sự đã đọc nó. Nhưng tôi không có ghi chép nào để chứng minh nó không bị đọc. "Có thể đã bị lấy" và "thực sự đã bị lấy" là hai chuyện khác nhau, nhưng riêng điều trước đã là một thiếu sót nghiêm trọng đối với một quán.

Khi truy ngược nguyên nhân, mọi thứ quy về cách biểu mẫu đặt chỗ được dựng. Để tính số chỗ trống, biểu mẫu tải 35 ngày dữ liệu đặt chỗ trực tiếp từ màn hình. Nếu màn hình đọc được, thì bất kỳ ai biết cách dựng những màn hình như thế cũng đọc được cùng dữ liệu đó. Đó là kết quả của một nền móng đầu tiên xây theo cảm giác, đạt mục tiêu "hiển thị chỗ trống" bằng con đường ngắn nhất.

Tôi cũng phát hiện địa chỉ email để thông báo cho quản trị viên của quán đang công khai, và bất kỳ ai cũng có thể ghi vào nơi lưu các bản dịch, nghĩa là dữ liệu có thể bị phá hoại hoặc chi phí bị đẩy lên.

Thứ tự sửa rất quan trọng. Nếu đột ngột chặn quyền đọc, biểu mẫu đặt chỗ sẽ không còn hiển thị được chỗ trống và ngừng hoạt động. Vì vậy trước hết tôi chuyển phép tính chỗ trống sang một điểm cuối phía máy chủ. Tiếp theo tôi đổi màn hình hoàn tất đặt chỗ để nó cũng chỉ lấy từ máy chủ thông tin cần thiết. Cuối cùng, tôi đóng việc đọc từ bên ngoài. Tôi sửa theo bốn giai đoạn theo thứ tự này và áp dụng vào hoạt động thật.

Sau khi sửa, tôi dùng máy để kiểm tra nó đã thực sự đóng. Tôi chuẩn bị một bài kiểm thử thử đọc dữ liệu đặt chỗ mà không xác thực, và chạy tự động sau mỗi thay đổi để xác nhận nó luôn bị từ chối. Tôi không sửa một lần rồi coi như xong. Tôi thiết lập để một phép kiểm tra luôn canh chừng, bảo đảm nó không bao giờ mở ra trở lại.

#### Dữ liệu khách thật còn sót lại trong lịch sử phát triển

Sau đó tôi nhờ AI kiểm tra toàn bộ kho mã (nơi lưu trữ chương trình), và một vấn đề nghiêm trọng hơn nữa xuất hiện.

Trong lúc phát triển, một tệp chứa dữ liệu của khách thật (địa chỉ email và số điện thoại từ 55 lượt đặt chỗ) đã bị gửi lên kho mã, vẫn nằm trong lịch sử thay đổi của chương trình. Kho mã là riêng tư, nhưng vì nó còn lại trong bản ghi, tôi không thể để mặc.

Tôi gỡ tệp đó khỏi toàn bộ lịch sử thay đổi, viết lại lịch sử và lưu lại. Dù vậy, các bản ghi cũ từ trước khi viết lại có thể vẫn còn ở phía GitHub, nơi lưu trữ kho mã. Vì vậy tôi đã đề nghị bộ phận hỗ trợ của GitHub xóa chúng, và xác nhận việc đó đã xong.

Cuộc kiểm tra cũng tìm ra những vấn đề khác: điểm cuối dịch thuật có thể dùng mà không cần xác thực, đăng nhập quản trị viên có thể bị tấn công dò mật khẩu hàng loạt, và có một khoảng thời gian trong đó, nếu bật lại thanh toán, một lượt đặt chỗ có thể được xác nhận khi còn chưa thanh toán. Tôi sửa từng cái một, bắt đầu từ cái nghiêm trọng nhất.

#### Không có bài kiểm thử tự động nào

Cuộc kiểm tra còn cho thấy thêm một sự thật. Hệ thống đặt chỗ không có lấy một bài kiểm thử tự động.

Kiểm thử tự động là một cơ chế trong đó máy tự động kiểm tra chương trình có hoạt động đúng không. Không có kiểm thử, khi bạn sửa một chỗ, bạn không có cách nào kiểm tra xem có chỗ khác bị hỏng không. Mỗi lần thêm một tính năng, ở đâu đó lại lặng lẽ hỏng một thứ. Đó chính xác là tình trạng trong giai đoạn tôi xây theo cảm giác.

Vì vậy tôi xây lại nền tảng kiểm thử từ con số không. Tôi đưa vào một hệ thống (CI) tự động chạy bốn phép kiểm tra sau mỗi thay đổi: kiểm tra kiểu, kiểm tra phong cách mã, kiểm thử và dựng bản build. Những quyết định quan trọng như tính giá, kiểm tra điều kiện đặt chỗ, liên kết hội viên và phát phiếu giảm giá được tách khỏi các chương trình màn hình để có thể được xác minh độc lập. Các quy tắc đọc và ghi cơ sở dữ liệu cũng được kiểm tra trong một môi trường kiểm thử mô phỏng cơ sở dữ liệu thật. Các bài kiểm thử đơn vị bắt đầu từ 275 và về sau tăng vượt 500.

Có một điều kiện tôi luôn đặt ra cho kiểm thử: "phá nó đi và xác nhận nó thất bại." Ngay cả khi một bài kiểm thử chuyển xanh (đạt), bạn cũng không biết bài kiểm thử đó có thực sự bắt được vấn đề hay không. Chỉ sau khi tôi cố ý phá chương trình và xác nhận bài kiểm thử chuyển đỏ (thất bại) thì tôi mới tin bài kiểm thử. Đó là vì những bài kiểm thử do AI viết đôi khi không kiểm tra gì cả.

#### Tám lỗ hổng trong biểu mẫu đặt chỗ

Sau khi nền tảng kiểm thử đã có, tôi nhờ AI xem xét lại toàn bộ quy trình đặt chỗ. Nó tìm ra tám vấn đề gây hại thật sự.

Nghiêm trọng nhất là việc bấm nút gửi liên tiếp tạo ra đặt chỗ trùng. Điều này thực tế đã từng xảy ra trong hoạt động thật. Tôi sửa bằng một cơ chế chỉ xử lý cùng một thao tác một lần dù nó đến hai lần (tính lũy đẳng, idempotency). Các vấn đề còn lại là: không xác nhận được lượt đặt chỗ nếu còn sót thông tin về một món đã xóa trong thực đơn; có một kẽ hở trong phép kiểm tra kín chỗ để lại chỗ cho việc vượt sức chứa; không ai nhận ra khi một email xác nhận gửi thất bại; dữ liệu nhập không được kiểm tra phía máy chủ; thông báo lỗi kỹ thuật nội bộ hiện lên màn hình khi có lỗi; chữ trong các ô nhập nhỏ đến mức màn hình tự phóng to trên iPhone; và chức năng tự điền cho phần nhập không hoạt động.

Với các email lỗi, tôi làm cho có thể phát hiện chúng trong màn hình quản trị và gửi lại. Trong lúc điều tra đó, tôi cũng phát hiện nhật ký kiểm toán ghi lại các lần xác nhận đặt chỗ đã thất bại mọi lần, từ rất lâu trước khi sửa, và không ghi lại gì cả.

Tôi sửa từng cái một và áp dụng vào hoạt động thật.

#### Đừng bao giờ bỏ qua việc xác minh mã do AI viết

Điều tôi học được từ trải nghiệm này là chính vì một chương trình do AI viết, bạn không được bỏ qua việc xác minh.

AI nhanh chóng định hình những gì được nói với nó. Nhưng sự cân nhắc dành cho những điều không được nói, như "làm cho nó không đọc được từ bên ngoài" hay "coi việc gửi hai lần là một", sẽ không có trừ khi bạn chỉ dẫn. Và những lỗ hổng như vậy nằm lặng lẽ bên trong các chương trình trông như đang chạy.

Con người không cần đọc toàn bộ mã. Việc chương trình có đúng hay không được canh chừng bằng các phép kiểm tra của máy và bằng cuộc kiểm tra của một AI khác. Việc kết quả có phù hợp với mục đích của quán hay không do chủ quán canh chừng. Bạn không cần đọc, nhưng không được bỏ qua việc xác minh. Tôi tin đó là ý nghĩa của việc xây dựng cùng một AI kiểu tác tử.

【Hình 2-3】Các quy tắc khi có thể đọc từ bên ngoài, và các quy tắc sau khi sửa (trích) *(Màn hình hiển thị bằng tiếng Nhật.)*

### 2-4 Xây theo cảm giác làm mâu thuẫn nhân lên

Càng thêm tính năng, càng có nhiều phần mâu thuẫn với những gì tôi đã quyết định trước đó.

Trường hợp điển hình là việc tính giảm giá. Trong biểu mẫu đặt chỗ, màn hình xác nhận, email và màn hình quản trị, phép tính giảm giá được viết riêng ở từng nơi. Nếu tôi đổi một quy tắc giảm giá ở một chỗ, một chỗ khác vẫn tính theo quy tắc cũ. Với cùng một lượt đặt chỗ, màn hình và email có thể hiển thị những số tiền khác nhau.

Về sau, tôi gom việc tính giá vào một tệp duy nhất. Biểu mẫu đặt chỗ, khung trò chuyện và máy chủ MCP đều đưa ra giá từ đó.

Các quy tắc cộng dồn giảm giá cũng thay đổi dọc đường. Như tôi đã viết ở Chương 1, Happy Hour ban đầu định cho kết hợp với các giảm giá khác, nhưng tôi thấy nó sẽ không có lãi và đổi sang không kết hợp được. Mỗi khi một quy tắc đổi, một người phải nhớ phải sửa ở những đâu. Đó là điểm yếu của một hệ thống xây theo cảm giác.

Cũng có sự lệch giữa môi trường kiểm thử và hoạt động thật. Trong lúc kiểm thử khung trò chuyện, một câu hỏi, "Chẳng phải có cái gì đó giảm 10% sao?", cho thấy các quy tắc giảm giá trong môi trường kiểm thử đã lệch khỏi hoạt động thật. Nếu các giá trị trong môi trường kiểm thử khác với hoạt động thật, bạn có thể vượt qua kiểm thử mà vẫn sai trong hoạt động thật. Điều tôi quyết định lúc đó là nguyên tắc "hoạt động thật là đúng". Từ đó, trước mỗi lần chạy kiểm thử, tôi sao chép các thiết lập của hoạt động thật vào môi trường kiểm thử và xác nhận độ lệch bằng không rồi mới chạy.

AI xây những gì được bảo. Nhưng nó không nhận ra các mâu thuẫn với những quyết định trước đó. Thứ ngăn mâu thuẫn không phải là AI. Đó là việc quyết định mọi thứ từ trước.

### 2-5 Học lại việc xác định yêu cầu

Sau khi nhìn lại hệ thống đặt chỗ tôi xây theo cảm giác, tôi học lại việc xác định yêu cầu. Xác định yêu cầu nghĩa là, trước khi xây, quyết định bạn sẽ xây cái gì, sẽ không xây cái gì, và ai sẽ dùng nó và dùng thế nào, rồi viết ra thành một tài liệu.

Đó là việc tôi làm như lẽ đương nhiên hồi còn là kỹ sư hệ thống. Nhưng khi đã có thể xây bằng AI, tôi đã bỏ qua nó mà không nhận ra. Kể cho nó một ý tưởng và trong vài phút một thứ chạy được xuất hiện. Trong tốc độ ấy, tôi đã cắt đi công sức quyết định.

Cách xây dựng của tôi bây giờ có ba giai đoạn.

