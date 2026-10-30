### 1-5 Qua các con số: khoảng 88% lượt đặt chỗ là đặt ngay trong ngày

Khi cứ thêm các cơ chế, tôi nhận ra một điều. Tôi không biết cơ chế nào đang phát huy tác dụng.

Vì vậy tôi đếm dữ liệu đặt chỗ. Trong 244 lượt đặt chỗ của 90 ngày gần nhất, có 215 lượt là đặt ngay trong ngày. Đó là 88,1%. Trung bình là 2,71 lượt đặt chỗ mỗi ngày.

Tamuro không phải nơi người ta đặt chỗ trước, mà là nơi người ta đến theo hứng. Điều đó chỉ trở nên rõ ràng khi tôi chuyển nó thành con số.

Từ những con số này, hai điều đã hiện ra.

Một là cách dựng biểu mẫu đặt chỗ. Nếu phần lớn lượt đặt là cho chính ngày hôm nay, sẽ tiện hơn nếu khung giờ trống gần nhất trong ngày đã được chọn sẵn khi màn hình đặt chỗ mở ra. Mặt khác, một số người muốn đặt cho ngày sau lại vô ý gửi nó thành hôm nay. Vì vậy tôi làm cho hôm nay nổi bật trên lịch, và trên màn hình xác nhận tôi hiển thị ngày giờ thật lớn kèm chữ "Hôm nay". Tôi giữ sự tiện lợi của việc chọn ngay trong ngày, đồng thời làm cho nhầm lẫn dễ được nhận ra.

Điều còn lại là ý nghĩa của giảm giá đặt sớm. Nhiều lượt đặt trong ngày nghĩa là chúng ta không đoán được doanh thu tương lai. Chỉ riêng thời tiết xấu cũng đủ làm lượng khách ghé quán sụt giảm. Để tăng dù chỉ một chút số lượt đặt trước, cần nhiều người hơn dùng giảm giá đặt sớm. Nhận thức này về sau dẫn đến câu chuyện xây dựng một AI đăng bài thay cho chủ quán.

Để nhìn vào các con số, bạn cần một hệ thống để đếm. Trang đặt chỗ hoàn toàn không có phân tích lượt truy cập. Tôi không biết có bao nhiêu người đến trang đặt chỗ, bao nhiêu người bỏ dở giữa chừng, và bao nhiêu người hoàn tất. Vì vậy tôi thêm một hệ thống đếm ba giai đoạn: đã đến trang, đã quyết định chi tiết, đã hoàn tất đặt chỗ. Nó không ghi lại ai đã đến, chỉ ghi giai đoạn và thời điểm.

Sau đó nữa, tôi còn xây một hệ thống gửi email báo cáo hằng tuần tóm tắt các con số đặt chỗ. Tôi sẽ mô tả việc nó ra đời như thế nào ở mục 1-7.

【Hình 1-3a】Hôm nay nổi bật trên lịch *(Màn hình hiển thị bằng tiếng Nhật.)*

【Hình 1-3b】Trên màn hình xác nhận, ngày giờ hiện lớn kèm chữ "Hôm nay" *(Màn hình hiển thị bằng tiếng Nhật.)*

### 1-6 Quá nhiều suất để lựa chọn

Khi hệ thống giảm giá đã có, điều tiếp theo tôi muốn là tăng thêm các khung giờ và suất ăn bán được.

Khung 6 giờ chiều không đầy khách, nên tôi tạo một khung Happy Hour đến 7 giờ tối. Với những người đến sau khi đã ăn, tôi tạo một suất chỉ đồ uống không kèm bữa ăn. Suất ăn theo set (course) và lớp học nấu ăn, trước đây tổ chức hằng tháng, tôi chuyển thành các sự kiện theo yêu cầu, chỉ mở khi có người đăng ký, nhận qua trang đặt chỗ. Để bán khoảng thời gian trước giờ mở cửa vào cuối tuần, từ 3 giờ 30 chiều, tôi tạo một suất tiệc cho nhóm từ sáu người trở lên.

Mỗi thứ đều có lý do. Lấy suất tiệc làm ví dụ: nếu tôi làm cho nó trông rẻ về giá, nó sẽ chỉ kéo vào những khách vốn đang chọn suất tiêu chuẩn, và doanh thu sẽ giảm. Vì vậy tôi đặt sự khác biệt không ở giá mà ở khung giờ trước giờ mở cửa, vốn chưa bao giờ mang lại doanh thu nào. Giảm giá Happy Hour không có lãi nếu kết hợp với các giảm giá khác, nên tôi quyết định không cho kết hợp.

Cứ thế, các suất ăn ngày càng tăng lên. Tiêu chuẩn, Cao cấp, Rất vui được gặp, Chào mừng quay lại, Giờ vui vẻ, Chỉ đồ uống, Suất ăn theo set, Lớp học nấu ăn, Tiệc. Mỗi suất có điều kiện về số người, có suất nhận giảm giá và có suất không, và có các hạn chế về giờ.

Một ngày nọ, tôi mở biểu mẫu đặt chỗ và nhận ra: như thế này thì khách làm sao mà chọn nổi.

Tôi, người xây dựng, hiểu mọi khác biệt. Nhưng liệu một người lần đầu mở trang đặt chỗ có thể so sánh chín suất và các điều kiện giảm giá của chúng rồi chọn được suất phù hợp với mình không? Nếu không, họ sẽ bỏ cuộc giữa chừng khi đặt. Những suất ăn tôi đã cất công thêm vào có thể rốt cuộc lại làm giảm số lượt đặt chỗ.

Tôi có thể dọn dẹp lại cho gọn. Nhưng mỗi suất đều có một khung giờ tôi muốn bán và một loại khách tôi muốn gặp. Tôi không muốn cắt suất nào.

Vì vậy tôi nghĩ ra một hệ thống trong đó khách hỏi ý kiến AI để quyết định chọn suất nào. Nói cho nó số người, ngày giờ bạn muốn đến, và cách bạn muốn tận hưởng thời gian tại quán, rồi AI đưa ra suất và mức giá phù hợp và dẫn bạn thẳng đến bước đặt chỗ. Quán gánh phần phức tạp của các suất ăn. Điều còn lại cho khách chỉ là một cuộc trò chuyện.

Hệ thống này là "T-AI-MURO" mà tôi viết ở mục 1-8. Trước đó, còn một điều nữa tôi nhận ra trong giai đoạn này.

【Hình 1-2】Chọn suất ăn trên biểu mẫu đặt chỗ. Có chừng này thẻ xếp thành hàng *(Màn hình hiển thị bằng tiếng Nhật.)*

### 1-7 "Việc này có thật sự mang khách đến không?"

Vào ngày tôi thêm suất tiệc, tôi dành cả ngày để liên tục thực hiện hết cải tiến này đến cải tiến khác cho trang đặt chỗ. Tôi làm gọn phần đầu trang, cho khớp thiết kế email, và đổi AI tạo chủ đề trò chuyện cho khách trong quán.

Buổi tối, một câu hỏi bất chợt đến với tôi.

"Những việc này có thật sự giúp mang thêm khách đến không?"

Khi tôi hỏi AI, nó đã phân loại các cải tiến của ngày hôm đó một cách trung thực.

| Phân loại | Các cải tiến của ngày hôm đó |
| --- | --- |
| Những thứ có thể tạo ra lượt đặt chỗ mới | Suất tiệc, khung 3 giờ 30 chiều vào cuối tuần và ngày lễ |
| Những thứ nâng tỷ lệ hoàn tất đặt chỗ của người truy cập trang | Làm gọn phần đầu trang, căn chỉnh các thẻ |
| Những thứ khuyến khích quay lại | Thống nhất thiết kế email |
| Những thứ không giúp mang khách đến | Đổi AI tạo chủ đề trò chuyện, liên kết đến điểm dừng tiếp theo, thông báo về Agenda |

Trong các cải tiến của ngày hôm đó, chỉ suất tiệc và khung 3 giờ 30 chiều dẫn trực tiếp đến việc mang khách đến. Phần còn lại là những cải tiến để không đánh mất những người đã truy cập trang rồi. Chúng cũng quan trọng, nhưng không làm tăng số khách.

Còn một vấn đề lớn hơn. Tôi không có cách nào để đo xem các cải tiến đó có hiệu quả hay không. Không có con số nào nối giữa "tôi đã cải tiến" và "khách đã tăng".

Câu trả lời của tôi gói trong một cụm: "Hãy xây một cái."

Vì vậy tôi bắt tay làm một báo cáo thu hút khách hằng tuần. Số lượt đặt chỗ, số khách, tổng số tiền, số lượt hủy. Phân tích theo ngày trong tuần và theo khung giờ trong ngày. Tỷ lệ khách lần đầu so với khách quay lại. Số lượng của các khung tiệc và 3 giờ 30 chiều. Lượt đặt chỗ đến từ đâu (biểu mẫu đặt chỗ, khung trò chuyện, lượt đặt từ AI, lượt nhập tay của quán). Số lượt bấm trong email, và số lượt đặt chỗ trong vòng bảy ngày sau những lượt bấm đó.

Con số nào cũng gắn liền với thời gian. Cũng trong ngày hôm đó, tôi phát hiện thêm một lỗ hổng. Tôi đã đặt lớp học nấu ăn và khung 3 giờ 30 chiều của suất tiệc là "cuối tuần", nhưng khi tôi tự hỏi "Còn ngày lễ thì sao?" và tìm hiểu, hệ thống đặt chỗ hoàn toàn không có khái niệm ngày lễ. Vào thứ Hai nghỉ lễ quán vẫn mở cửa, thế mà khung 3 giờ 30 chiều không xuất hiện. Tôi đưa cho nó một danh sách ngày lễ và sửa để xử lý chúng như cuối tuần. Đó là một lỗ hổng mà không ai nhận ra cho tới khi chính người xây dựng nhận ra.

Trước khi xây báo cáo, tôi bịt trước các lỗ hổng liên quan đến thời gian.

Ngay cả những khách quen đã đến từ trước khi tôi dùng hệ thống đặt chỗ cũng trông như "khách lần đầu" trong dữ liệu ghi lại. Vì vậy trong báo cáo tôi viết "lần ghé đầu tiên trong dữ liệu" và luôn kèm theo ngày dữ liệu bắt đầu. Để đánh giá một cải tiến có hiệu quả hay không, bạn cần bức tranh trước khi cải tiến. Với báo cáo đầu tiên, tôi tổng hợp ngược lại tám tuần vừa qua và dùng đó làm mốc cơ sở. Trong tuần quán tạm đóng cửa, vì đi xa hoặc lý do khác, số lượt đặt chỗ giảm là điều đương nhiên. Vì vậy tôi cũng ghi số ngày kinh doanh, để có thể so sánh theo từng ngày kinh doanh.

Mục "Những thay đổi đáng chú ý" tôi thôi không để AI viết, mà cho chạy theo các phép tính cố định và những câu văn cố định. Làm vậy để chi phí hằng tuần giữ ở mức không. Tên và thông tin liên lạc của khách không xuất hiện trong báo cáo; chỉ hiển thị số lượng và tỷ lệ.

Một khi đã xây được cách đo, chính cách tôi xây các cải tiến cũng thay đổi. Tôi bắt đầu quyết định ngay từ đầu một cải tiến cùng với phương pháp đo hiệu quả của nó. Việc đo không phải thứ để nghĩ đến sau khi cải tiến; nó nằm trong cùng tài liệu chỉ dẫn với cải tiến. Đó là điều tôi học được vào ngày hôm đó.

【Hình 1-6】Báo cáo thu hút khách hằng tuần gửi đến mỗi tuần (dữ liệu tổng hợp) *(Màn hình hiển thị bằng tiếng Nhật.)*

### 1-8 Một khung trò chuyện với quán: "T-AI-MURO"

Như tôi đã viết ở mục 1-6, các suất ăn đã nhân lên, và biểu mẫu đặt chỗ trở nên khó chọn với người ghé lần đầu. Và khách lần đầu muốn biết nhiều hơn các suất ăn và ngày giờ. Nơi này có bầu không khí thế nào? Đi một mình có thấy lạc lõng không? Chủ quán là người thế nào? Mang trẻ em theo có được không? Nếu bạn cứ xếp các nút đặt chỗ mà không trả lời những câu hỏi như vậy, bạn không thể thúc đẩy những người còn đang đắn đo đưa ra quyết định.

Vì vậy tôi quyết định đặt một "khung trò chuyện với quán" lên trang đặt chỗ. Khi khách viết một câu hỏi, AI trả lời với tư cách là quán. Nếu số người và ngày giờ được chốt trong lúc trò chuyện, khách có thể đi thẳng đến màn hình xác nhận đặt chỗ. Nó có tên là "T-AI-MURO", và trong cuộc trò chuyện nó tự giới thiệu là "Tamuro". T-AI-MURO nói với tư cách chính quán, và nhắc đến chủ quán ở ngôi thứ ba.

Khách gần như không phải gõ gì. Họ chỉ chạm vào các lựa chọn T-AI-MURO đưa ra, và cuộc trò chuyện tiến lên. Điều đó có nghĩa là các lựa chọn nó đưa ra tiếp theo quyết định chất lượng cuộc trò chuyện. Tôi luôn trộn ba loại nước đi vào các lựa chọn: những nước đi hướng đến đặt chỗ (số người, giá, khung giờ trống, ngày giờ), những nước đi hướng đến việc tìm hiểu quán (bầu không khí, chủ quán, khách là những ai, có trò chuyện được với người ngồi bên cạnh không), và những nước đi nảy sinh từ mạch trò chuyện. Đưa người ta đến lượt đặt chỗ không phải là mục tiêu duy nhất. Để họ biết về bầu không khí của quán và chủ quán cũng là cốt lõi của khung trò chuyện này.

Riêng giá thì tôi quyết định không để AI tính. Không có gì đảm bảo AI luôn tính đúng, lần nào cũng đúng, cách các mức giảm giá cộng dồn hay các bậc theo số người được áp dụng. Chương trình đưa ra giá và khung giờ trống bằng các phép tính cố định, còn AI giữ đúng việc diễn đạt chúng thành lời.

#### Kiến thức đầu tiên đến từ những bài đăng trước đây của chính tôi

Để T-AI-MURO trả lời được các câu hỏi về quán, nó cần có kiến thức về quán. Làm tư liệu, tôi xuất toàn bộ những bài tôi đã viết từ trước đến nay trên Instagram và X (trước đây là Twitter) và dùng chúng. Từ đó, tôi dựng những câu hỏi khách có khả năng hỏi, cùng các câu trả lời.

Khi thử thật, các bài đăng trên X hóa ra hữu ích làm tư liệu hơn Instagram. Instagram phần lớn là ảnh, ít chữ. Trên X, tôi đã để lại những ghi chép bằng lời của mình về món ăn, về quán và về điều tôi đang nghĩ.

#### Chỉ 9 trong 36 kịch bản đạt

Trước khi đưa T-AI-MURO vào hoạt động thật, tôi kiểm thử xem nó trả lời đúng đến mức nào. Tôi cũng để AI chạy các bài kiểm thử. Tôi đưa cho một AI đóng vai khách một tính cách và một mục đích, rồi để nó trò chuyện với T-AI-MURO. Tôi chuẩn bị 36 kịch bản: "một mình tối nay", "4 người sau hai tuần", "đi cùng trẻ em", "dị ứng", "bao trọn quán", "thông báo đến muộn", "nguồn gốc tên quán", "chủ quán là người thế nào", v.v.

Kết quả vòng đầu: 9 trong 36 kịch bản đạt.

Câu trả lời xuất hiện nhiều nhất là "Xin lỗi, tôi chưa trả lời tốt được câu này." Câu trả lời này thậm chí xuất hiện với cả những câu hỏi về bầu không khí của quán và về chủ quán. Hễ xuất hiện các từ như "đặt chỗ", "hôm nay", "bao trọn quán" hay "chủ quán", một danh sách khung giờ trống lại hiện ra bất kể câu hỏi thực sự là về điều gì. Trong một số cuộc trò chuyện, tin nhắn báo đến muộn bị coi là một lượt đặt chỗ mới. Với một khách ăn chay, nó đưa ra ví dụ là các món xào có cá bào khô và súp miso. Nó thậm chí còn cung cấp bằng tiếng Anh thông tin về một đợt mua chung mà chúng tôi đã dừng rồi.

#### Tôi trả lời 11 câu hỏi, mỗi câu một dòng

Một phần nguyên nhân nằm ở cách chương trình được dựng. Chuyện đó tôi để dành cho Chương 2. Nguyên nhân còn lại thì đơn giản: những thông tin thực tế về quán còn thiếu. AI không thể trả lời điều nó không biết.

Vì vậy tôi gom những câu hỏi AI không trả lời được và quyết định tự trả lời chúng, mỗi câu một dòng.

Bạn có thể vào mà không cần đặt chỗ. Trẻ em dưới tuổi tiểu học thì khó tiếp đón. Hủy và đổi lịch chậm nhất trước một ngày, qua email, điện thoại hoặc tin nhắn mạng xã hội. Báo đến muộn xin gọi điện thoại. Có khu hút thuốc bên ngoài quán. Được mang đồ uống từ bên ngoài vào, có tính phí mở chai (corkage). Có thể bao trọn quán tùy mức giá và thời gian, tối đa 19 người. Các yêu cầu ăn uống đặc biệt (dị ứng, kiêng cữ) và dịp kỷ niệm chúng tôi sẽ cố gắng đáp ứng hết mức có thể, nên xin hãy trao đổi trước. Chủ quán có mặt ở quán hầu như mọi ngày kinh doanh. Khoảng mỗi năm một lần có kế hoạch tổ chức lễ hội yukata.

Chỉ vậy thôi. Chỉ bằng cách trả lời 11 câu hỏi, mỗi câu một dòng, ở lần kiểm thử thứ hai đã có 24 trong 36 kịch bản đạt.

| Câu hỏi | Câu trả lời lần đầu | Câu trả lời lần hai |
| --- | --- | --- |
| Đi cùng trẻ con có được không? | Xin lỗi, tôi chưa trả lời tốt được câu này | Trẻ từ tuổi tiểu học trở lên có thể tiếp đón nếu trao đổi trước. Dưới tuổi tiểu học thì khó |
| Không đặt chỗ có vào được không? | (danh sách khung giờ trống) | Bạn có thể vào mà không cần đặt chỗ |
| Hôm nay chủ quán có ở quán không? | (danh sách khung giờ trống) | Chủ quán có mặt ở quán hầu như mọi ngày kinh doanh. Hôm nay là ngày kinh doanh, nên dự kiến sẽ có mặt |
| Có phải chỗ yên tĩnh không? Toàn khách quen? | Xin lỗi, tôi chưa trả lời tốt được câu này | Đây là nơi để thư giãn. Khách dễ trò chuyện với nhau, và không phải chỗ ồn ào |

Tại đây bắt đầu hiện ra một khuôn mẫu. AI tự tạo ra các câu hỏi dự kiến, T-AI-MURO trả lời chúng, và chúng ta sửa các lỗi. Sau đó chỉ những câu hỏi không trả lời được vì thiếu thông tin thực tế về quán mới được chuyển cho chủ quán. Công sức của chủ quán chỉ là một dòng cho mỗi câu hỏi không trả lời được. Mọi thứ còn lại, AI vận hành.

#### Cảnh "ngân sách ¥5.000 (khoảng $33)" bị trượt

Tôi cũng gắn một phán quyết của AI vào các bài kiểm thử AI. Một AI khác đọc nhật ký cuộc trò chuyện và quyết định đạt hay không đạt.

Trong số đó có một kịch bản với một khách có "ngân sách là ¥5.000 (khoảng $33)". Phán quyết của AI là đạt. T-AI-MURO đã lịch sự đưa ra các suất trong ngân sách.

Nhưng khi tôi đọc, nó là không đạt. Nó đã không hỏi số người. Tamuro có giảm giá theo nhóm. Tùy số người, các suất bạn có thể chọn với cùng một ngân sách sẽ thay đổi.

Lúc đó, tôi phát biểu lại mục đích.

"Hướng đến nhóm đông nhất có thể, để thu về tổng số tiền nhiều nhất. Xác nhận số người. Mục tiêu cuối cùng là khiến khách đến. Càng đông càng tốt. Để tăng doanh thu."

Chỉ với một câu đó, toàn bộ thiết kế của cuộc trò chuyện thay đổi. Luôn xác nhận số người trước khi trả lời về giá, và trả lời bằng tổng số tiền. Ngay trước một bậc của giảm giá nhóm, thêm câu "thêm một người nữa là được giảm bao nhiêu phần trăm". Khi khách nêu ngân sách, hiển thị trước suất cao nhất trong ngân sách. Tuy nhiên, khách đi một mình chiếm một nửa số khách của quán, nên với khách đi một người thì không gợi ý tăng số người.

Khi bạn để AI chạy các bài kiểm thử AI, chúng chạy rất nhanh. Nhưng chính con người quyết định tiêu chuẩn để đạt. Bạn có nêu được mục đích trong một câu hay không. Điều đó quyết định chất lượng các cuộc trò chuyện của AI.

#### Mong muốn của khách được ưu tiên hơn lời gợi ý của quán

Còn một cảnh nữa tôi vạch ra một ranh giới quan trọng.

Trong lúc kiểm thử, tôi phát hiện một vấn đề: mọi lượt đặt chỗ đều bị đẩy sang suất rẻ nhất. Khi tôi sửa, lần này gần như tất cả thành suất Tiêu chuẩn, và tổng số tiền trung bình nhảy lên gần gấp đôi. Tôi suýt thì mừng, nhưng nhìn kỹ thì AI đóng vai khách chỉ đơn giản là lần nào cũng bấm lựa chọn đầu tiên. Ngay cả những khách nói "rẻ nhất là được rồi" cũng được gợi ý suất Tiêu chuẩn.

Tại đây tôi đặt ra một nguyên tắc. Điều khách nêu rõ là mong muốn (phương án rẻ nhất, một mức ngân sách, tên một suất ăn) luôn được ưu tiên hơn lời gợi ý của quán. Lời gợi ý của quán chỉ dành cho lúc khách chưa nói gì.

Mục tiêu tăng doanh thu của quán và lòng tin của khách có thể xung đột với nhau chỉ vì một cách gợi ý không khéo. Nếu mất lòng tin, chính số lượt ghé sẽ giảm. Chính chủ quán, chứ không phải AI, là người vạch được ranh giới này.

Về sau, khi tôi huấn luyện lại T-AI-MURO bằng một lượng lớn câu hỏi, nguyên nhân phổ biến nhất của các sai sót là "phản ứng với từ ngữ và thực hiện một thao tác cố định trước khi trả lời câu hỏi". Ngay khi nghe các từ như "số người", "bao nhiêu" hay "một mình", nó bỏ qua câu hỏi và chuyển sang quy trình đặt chỗ hoặc lời gợi ý. Xét về dịch vụ, đó là một nhân viên thúc ép bán hàng mà không lắng nghe khách. Trả lời câu hỏi của khách trước. Điều cơ bản này của sự hiếu khách lại là thử thách lớn nhất, ngay cả với AI.

Vào đêm ngày 6 tháng 10 năm 2026, T-AI-MURO xuất hiện ở đầu trang đặt chỗ với tư cách lối vào chính thức. Vì có những khách không muốn đặt chỗ bằng trò chuyện, tôi vẫn giữ biểu mẫu đặt chỗ trước đó ở bên cạnh.

> Hãy thử: Mở trang đặt chỗ của Tamuro (https://tamuroreservation.vercel.app/?src=b2-vi-{{FMT}}) và hỏi T-AI-MURO "một mình tối nay". Cuộc trò chuyện sẽ dẫn bạn đến tình trạng còn chỗ và mức giá của hôm nay.

【Hình 1-4】Màn hình trò chuyện T-AI-MURO. Cuộc trò chuyện tiến lên chỉ bằng cách chạm vào các lựa chọn *(Màn hình hiển thị bằng tiếng Nhật.)*

【Hình 1-10】Những câu hỏi chưa trả lời được dồn lại trong màn hình quản trị (dữ liệu tổng hợp) *(Màn hình hiển thị bằng tiếng Nhật.)*

### 1-9 Và rồi, từ AI của khách

Nhờ xây T-AI-MURO, trang đặt chỗ của Tamuro có được khả năng "trả lời các câu hỏi về quán qua trò chuyện, cho xem giá và khung giờ trống, và dẫn dắt khách cho đến khi đặt chỗ xong".

Điều tôi nghĩ đến tiếp theo là làm cho việc tương tự có thể thực hiện từ chính AI của khách.

T-AI-MURO chỉ có thể trò chuyện với những người đến trang đặt chỗ của Tamuro. Nhưng nhiều người hỏi ý kiến AI họ dùng mỗi ngày trước tiên. Nếu AI đó không biết về Tamuro, Tamuro thậm chí không xuất hiện trong danh sách gợi ý. Thay vì chờ khách đến trang của Tamuro, hãy mở khung của Tamuro ở phía AI của khách. Đó là máy chủ MCP.

Thành thật mà nói, lúc đầu tôi đã do dự về việc xây nó. Ở thời điểm này, không có nhiều người đặt chỗ nhà hàng từ chính AI của mình. Cho rằng không thể kỳ vọng lượt đặt chỗ tăng trực tiếp, có lần tôi đã hạ mức ưu tiên của nó và tạm gác lại.

Tôi vẫn quyết định xây vì tôi nghĩ việc lối vào thay đổi chỉ còn là vấn đề thời gian. Như tôi đã viết ở đầu, vào tháng 8 năm 2026 đã có thể đặt chỗ từ ChatGPT thông qua một dịch vụ đặt chỗ lớn. Sớm muộn, việc nhờ AI tìm nhà hàng cho mình sẽ là chuyện bình thường. Khi điều đó xảy ra, các quán nhỏ không có tên trên những dịch vụ lớn sẽ rơi khỏi tầm nhìn của AI. Vì vậy, hãy mở cửa sổ trước khi lối vào thay đổi.

Những gì tôi quyết định cho phiên bản đầu tiên rất hẹp. Nó chỉ cần làm giống khung trò chuyện trên trang đặt chỗ (T-AI-MURO). Nó chỉ có thể đọc thông tin của quán, khung giờ trống và giá, rồi trao lại URL của một trang đặt chỗ với các điều kiện đã điền sẵn. Việc xác nhận đặt chỗ do chính khách thực hiện trên trang của Tamuro. AI của khách không tự xác nhận một lượt đặt chỗ. Thao tác bấm nút quyết định cuối cùng vẫn do con người thực hiện.

Hãy quay lại cảnh mở đầu.

Vào một buổi chiều thứ Sáu, một khách hỏi AI của mình: "Ở Higashi-Nakano có chỗ nào tối nay mình uống một mình được không?" AI truy vấn khung của Tamuro. Hệ thống đặt chỗ của Tamuro trả về các khung giờ trống của tối nay, cùng với suất ăn và mức giá phù hợp với một khách đi một mình. AI nói lại cho khách, và đưa ra một trang đặt chỗ của Tamuro với ngày giờ và số người đã điền sẵn.

Mọi điều tôi đã viết trong chương này đều là nền tảng hậu thuẫn cho chuỗi bước đó. Hệ thống giảm giá xây cùng với đợt tăng giá. Hệ thống chăm sóc khách quen. Dữ liệu cho thấy phần lớn lượt đặt chỗ được thực hiện ngay trong ngày. Vốn hiểu biết về quán được bồi đắp nhờ trả lời 11 câu hỏi, mỗi câu một dòng. Nguyên tắc đặt mong muốn của khách lên trước lời gợi ý của quán.

Một quán được đặt chỗ qua AI không được dựng nên trong một đêm. Nó đứng trên sự tích lũy của những hệ thống nhỏ, được thêm vào từng cái một, được kiểm thử, bị bỏ đi và được sửa.

> Hãy thử: Đăng ký máy chủ MCP của Tamuro (https://tamuroreservation.vercel.app/api/mcp) vào AI của chính bạn và hỏi: "Tối nay Tamuro còn chỗ không?" Cách đăng ký được viết trong phần Lời kết.

### 1-10 Những gì tôi đã xây dựng, và những gì có hiệu quả

Trong chương này, tôi đã kể về việc xây dựng nhiều hệ thống. Nhưng "tôi đã xây được" và "việc kinh doanh đã thay đổi" là hai chuyện khác nhau. Ở cuối chương, tôi sẽ tách bạch hai điều đó.

Những gì có thể xác nhận bằng con số. Rằng 88,1% lượt đặt chỗ là đặt ngay trong ngày. Rằng tỷ lệ đạt của khung trò chuyện tăng từ 9 lên 24 chỉ nhờ thêm 11 mục thông tin thực tế về quán. Rằng tỷ lệ đạt của phần hướng dẫn về giá và suất ăn tăng từ 29,4% lên 42,7% sau các lần sửa. Đây là những sự thật có ghi lại.

