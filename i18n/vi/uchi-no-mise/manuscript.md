# Làm riêng cho quán bar của mình

Ghi chép của chủ một quán bar 19 chỗ ngồi tự xây dựng mọi thứ, từ hệ thống đặt chỗ đến các công cụ, cùng AI

Raku Bonta

Loạt Agenda: https://bontallc.com/agenda?via=b2-vi-{{FMT}}

Instagram của Tamuro: https://www.instagram.com/tamuro.higashinakano/

Trang đặt chỗ của Tamuro: https://tamuroreservation.vercel.app/?src=b2-vi-{{FMT}}

## Lời mở đầu

Cuốn sách này là bản ghi chép chân thực về cách chủ một quán bar 19 chỗ ở Higashi-Nakano *(một khu dân cư phía tây Tokyo, nằm ngay phía tây Shinjuku)*, Tokyo, vận hành quán với sự giúp đỡ của AI.

Quán bar có tên là "Tamuro". Cái tên này nghĩa là nơi mọi người tụ họp. Quán mở cửa vào tháng 11 năm 2018, một chốn nhỏ với 11 chỗ ngồi ở quầy và 8 chỗ ngồi trên chiếu tatami. Ban ngày, ngay trong không gian ấy, một nhân viên của quán điều hành một tiệm cơm cà ri hamburger tên là "Quatre Épices".

Trong cuốn sách trước, *Phó quản lý AI*, tôi viết về chính AI tạo sinh. Trong khoảng một năm kể từ đó, AI đã chuyển từ một công cụ trả lời câu hỏi thành một công cụ làm xong việc thay bạn. Chỉ cần đưa ra chỉ dẫn, nó viết chương trình, kiểm thử, sửa lỗi của chính mình và hoàn tất công việc. Chúng ta gọi loại AI này là AI tác tử (agentic AI).

Nhờ AI tác tử, tôi tự xây dựng hệ thống đặt chỗ của Tamuro. Tôi xây một hệ thống giảm giá đi kèm với đợt tăng giá. Tôi xây một hệ thống chăm sóc khách quen. Tôi xây một AI trả lời các câu hỏi của khách. Và cuối cùng, hệ thống đã phát triển đến mức khách hàng có thể hỏi Tamuro từ chính AI của mình rồi tiếp tục đặt chỗ.

Tôi cũng lấy những công cụ tiện dụng mình đã làm cho quán, chỉnh lại để các quán khác cũng dùng được, rồi bắt đầu cung cấp với giá vài trăm yên mỗi tháng. Đó là loạt Agenda.

Cuốn sách này mô tả những gì tôi đã xây dựng trong quá trình đó, những gì tôi đã thất bại, và những gì tôi phải học lại. Không chỉ có những câu chuyện thành công. Tôi cứ làm ra những thứ chạy được, theo hứng nhất thời, và các mâu thuẫn chồng chất dần. Về sau tôi phát hiện thông tin cá nhân của khách có thể bị đọc từ bên ngoài. AI đã tự bịa ra và viết như thể là thật những điều mà quán chưa từng nói. Tôi đưa những thất bại ấy vào đây đúng như chúng đã xảy ra.

### Cách đọc cuốn sách này

Cuốn sách này có năm chương.

| Chương | Nội dung | Phù hợp nhất với |
| --- | --- | --- |
| Chương 1 | Quán nhận đặt chỗ từ AI (khía cạnh kinh doanh của hệ thống đặt chỗ) | Mọi người |
| Chương 2 | Phía sau hệ thống đặt chỗ (kỹ thuật) | Người làm kỹ thuật và ai tò mò về công nghệ |
| Chương 3 | Chia sẻ công cụ của quán mình cho các quán khác (khía cạnh kinh doanh của loạt Agenda) | Mọi người |
| Chương 4 | Hệ thống để một mình xây dựng sản phẩm (kỹ thuật) | Người làm kỹ thuật và ai tò mò về công nghệ |
| Chương 5 | Tương lai của những quán nhỏ | Mọi người |

Chương 2 và Chương 4 mang tính kỹ thuật và dùng nhiều thuật ngữ chuyên môn hơn. Mỗi chương mở đầu bằng phần tóm tắt ba dòng về những điểm chính, nên nếu công nghệ không khiến bạn hứng thú, hãy chỉ đọc phần đó rồi sang chương tiếp theo. Đọc lần lượt Chương 1, 3 và 5, mạch chuyện vẫn hoàn toàn liền mạch.

Ở bất cứ chỗ nào có thể, tôi đều thêm lời giải thích dễ hiểu bên cạnh mỗi thuật ngữ kỹ thuật. Dù bạn chưa từng viết một chương trình nào, tôi hy vọng bạn sẽ cảm nhận được việc vận hành một quán cùng AI nghĩa là thế nào.

### Về tác giả

Tôi làm trong ngành CNTT khoảng 16 năm, chủ yếu ở mảng lập kế hoạch hệ thống và làm cầu nối giữa những người trực tiếp làm nghiệp vụ với các đơn vị phát triển phần mềm, rồi sau đó bước vào ngành ăn uống. Vì vậy, đây không phải câu chuyện về một người chưa từng viết một dòng mã nào mà tự xây dựng mọi thứ bằng AI. Tôi muốn thành thật về điều đó.

Dù vậy, giờ đây tôi có thể tự xây dựng và vận hành, một mình, vừa trực tiếp đứng quán phục vụ khách, một thứ có quy mô mà trước kia cần cả một đội ngũ và vốn liếng. Vài năm trước, điều đó là không thể tưởng tượng nổi. Tôi muốn mô tả thực tế của sự thay đổi ấy một cách cụ thể nhất có thể.

### Cuốn sách này được làm ra như thế nào

Cuốn sách này cũng được làm cùng AI. Xuất phát từ những ghi chép tôi lưu lại trong công việc phát triển hằng ngày, AI viết các bản nháp, còn tôi đọc, chỉnh sửa và đưa ra quyết định. Tôi cũng nhờ AI chụp các ảnh màn hình dùng làm hình minh họa.

Tôi đã đọc lại toàn bộ, nhưng văn bản do AI viết có thể lẫn những điều không đúng sự thật. Như tôi nói trong phần chính, AI nói "xong rồi", và kiểm tra điều đó là việc của con người. Có thể trong cuốn sách này có những lỗi mà tôi chưa phát hiện ra.

Ngoài ra, thông số kỹ thuật của các công cụ và dịch vụ AI thay đổi chỉ trong vài tháng. Các bước thực hiện, mức giá và tình trạng hỗ trợ của từng công ty được mô tả trong sách này là tính đến tháng 10 năm 2026. Khi tự mình thử, xin hãy kiểm tra thông tin chính thức vào thời điểm đó.

Nếu bạn phát hiện sai sót, tôi sẽ rất vui nếu bạn báo cho tôi trên note hoặc X. Phát hiện ra lỗi nào, tôi sẽ sửa dần lỗi đó.

### Ba hướng đi tiếp sau cuốn sách này

Cuốn sách này được đọc miễn phí dưới dạng PDF, trên note và trên Google Play. (Riêng trên Kindle, quy định của cửa hàng yêu cầu một mức giá tối thiểu.) Đổi lại, tôi đã chuẩn bị ba nơi bạn có thể đến sau khi đọc xong. Nếu chỉ một trong số đó có ích cho bạn, việc viết cuốn sách này đã xứng đáng.

1. Thử trong quán của chính bạn. Bạn có thể bắt đầu loạt Agenda với cuốn sổ miễn phí. https://bontallc.com/agenda?via=b2-vi-{{FMT}}
2. Theo dõi những gì tôi làm. Tôi viết về những công cụ tiếp theo mình xây dựng, và về cuộc sống thường ngày ở quán, trên note và X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Nếu có dịp đến Tokyo, mời bạn ghé Tamuro. Cách lối ra phía đông của ga Higashi-Nakano một phút. Bạn có thể vào mà không cần đặt chỗ. Trang đặt chỗ https://tamuroreservation.vercel.app/?src=b2-vi-{{FMT}}

## Chương 1: Quán nhận đặt chỗ từ AI

### 1-1 "Tối nay chỗ nào còn mở không?" Bạn hỏi AI

Vào một buổi chiều thứ Sáu, một người vừa tan làm nói chuyện với chiếc điện thoại thông minh của mình.

"Ở Higashi-Nakano có chỗ nào tối nay mình uống một mình được không? Chỗ nào đừng ồn quá."

Người trả lời không phải một người bạn. Đó là trợ lý AI mà người ấy dùng mỗi ngày. AI liệt kê các quán gợi ý, mô tả bầu không khí của từng quán, và cho biết giờ còn trống cùng mức giá của tối nay. Nếu có quán nào lọt vào mắt, họ có thể đi thẳng đến màn hình đặt chỗ.

Đây không phải chuyện của tương lai.

Vào ngày 10 tháng 8 năm 2026, OpenAI đã thêm tính năng đặt bàn nhà hàng vào ChatGPT. Theo ghi chú phát hành chính thức, tính năng này kết nối với các dịch vụ đặt chỗ OpenTable, Resy và Yelp, và các khung giờ còn trống hiện ngay bên trong câu trả lời của ChatGPT. Bạn cũng có thể đặt câu hỏi để thu hẹp lựa chọn, và khi đã chọn được giờ phù hợp, bạn có thể đặt luôn. Tính năng này bao gồm OpenTable trên toàn thế giới, Resy ở Mỹ, và Yelp ở Mỹ và Canada.

Nói cách khác, cánh cửa mà mọi người dùng để tìm nơi ăn uống đang bắt đầu chuyển từ công cụ tìm kiếm và các trang đánh giá nhà hàng sang "AI của riêng mình".

Nhưng có một điều kiện. Những quán duy nhất bạn đặt được qua ChatGPT là những quán đã đăng ký với các dịch vụ đặt chỗ lớn. Các quán nhỏ không có tên ở đó thì AI không nhìn thấy.

Vậy một quán bar 19 chỗ ở Higashi-Nakano không dùng các dịch vụ đặt chỗ lớn nên làm gì?

Tamuro chọn một con đường khác. Không đi qua các dịch vụ lớn, quán nối thẳng hệ thống đặt chỗ của riêng mình với AI.

Khi một khách hàng hỏi ChatGPT hay Claude của chính họ: "Tối nay Tamuro còn chỗ không?", AI sẽ truy vấn thẳng hệ thống đặt chỗ của Tamuro, kiểm tra giờ còn trống và mức giá rồi trả lời. Khi các điều kiện đã chốt, nó dẫn khách đến trang đặt chỗ của Tamuro với số người và ngày giờ đã điền sẵn. Khách tự bấm nút xác nhận cuối cùng.

"Điểm kết nối giữa AI và hệ thống của một quán" này được gọi là máy chủ MCP. MCP là viết tắt của Model Context Protocol, một bộ quy ước chung giúp AI dùng được các công cụ và dữ liệu bên ngoài. Tôi giải thích chi tiết ở Chương 2.

Thật ra, các dịch vụ đặt chỗ lớn cuối cùng cũng chuyển khách sang màn hình của chính họ. Với những lượt đặt cần thẻ tín dụng, quy trình được hoàn tất trên màn hình của OpenTable, còn việc thay đổi hay hủy sau khi đặt do phía mỗi dịch vụ xử lý. AI là lối vào, còn màn hình của dịch vụ đặt chỗ là nơi xác nhận. Cách Tamuro làm có cùng cấu trúc đó. Điểm khác duy nhất là không có công ty lớn nào đứng ở giữa.

Và người xây dựng hệ thống này không phải một công ty phát triển bên ngoài. Đó là tôi, chủ quán. Tôi đưa chỉ dẫn cho AI, nhờ AI viết chương trình, và nhờ AI chạy kiểm thử.

Tất nhiên, không phải ngay từ đầu tôi đã đạt được kết quả này. Mọi thứ bắt đầu từ một biểu mẫu đặt chỗ rất đơn giản. Rồi đến đợt tăng giá, rồi những ý tưởng giảm giá, rồi hệ thống chăm sóc khách quen, rồi những thất bại và việc xây dựng lại.

Trước hết, tôi xin mô tả Tamuro là nơi như thế nào trong năm dòng. Đi bộ một phút từ lối ra phía đông của ga Higashi-Nakano. 19 chỗ ngồi, 11 ở quầy và 8 trên chiếu tatami. Khoảng một nửa số khách đến một mình, và quầy giúp dễ bắt chuyện với người ngồi bên cạnh. Đồ ăn là sự kết hợp của bốn món khai vị và một món chính, và món được ưa chuộng nhất là tonteki (bít tết heo) đậm vị tỏi, hơi ngọt. Rượu vang chủ yếu từ Tây Ban Nha và Ý, và có khoảng 20 loại gin thủ công của Nhật. Bạn có thể vào mà không cần đặt chỗ.

Tôi cũng xin nêu một điều tôi nhắm tới. Tôi không muốn chỉ nhận đặt chỗ. Tôi muốn ngay cả một quán nhỏ cũng có thể tự tay xây dựng toàn bộ chuỗi từ việc được biết đến, thu hút người đến, cho tới khiến họ quay lại. Những đợt giảm giá, email và khung trò chuyện xuất hiện trong chương này đều là các bộ phận phục vụ một mục đích duy nhất ấy.

Trong chương này, tôi tua lại thời gian và lần theo cách hệ thống đặt chỗ của Tamuro đã lớn lên.

【Hình 1-1】Màn hình sau khi kết nối từ ChatGPT đến máy chủ MCP của Tamuro (ngày 10 tháng 10 năm 2026). Nó đọc thông tin của quán và trả lời rằng có thể xử lý giờ còn trống, các suất ăn theo set, mức giá và dẫn khách đến trang đặt chỗ *(Màn hình hiển thị bằng tiếng Nhật.)*

### 1-2 Điểm xuất phát: chỉ nhận đặt chỗ

[Trang đặt chỗ của Tamuro](https://tamuroreservation.vercel.app/?src=b2-vi-{{FMT}}) lúc đầu rất đơn giản. Chọn ngày, giờ và số người, nhập tên và thông tin liên lạc, rồi gửi. Quán nhận được thông báo. Chỉ có vậy.

Tôi xây phần nền đầu tiên bằng công cụ phát triển AI của Google (Antigravity). Tôi kể cho AI về từng tính năng mình nghĩ ra, và khi có thứ chạy được, tôi chuyển sang thứ tiếp theo. Đó là cái gọi là vibe coding (nói với AI bất cứ điều gì chợt nghĩ ra và để nó xây dựng theo cảm giác).

Với tôi lúc đó, hết bất ngờ này đến bất ngờ khác. Chỉ cần mô tả bố cục một màn hình bằng lời, nó thành hình trong vài phút. Bảo rằng muốn có lịch, thế là lịch hiện ra. Trong những khoảng trống khi đang điều hành quán, một trang đặt chỗ đã thành hình.

Tamuro là nơi bạn có thể vào mà không cần đặt chỗ. Thực tế, phần lớn lượt đặt chỗ được thực hiện ngay trong ngày, và nhiều khách cứ thế bước vào. Dù vậy, tôi vẫn xây hệ thống đặt chỗ vì tôi muốn có cách kết nối với khách trước khi họ đến. Khi ai đó đặt chỗ, tên và thông tin liên lạc của họ còn lại. Khi thông tin liên lạc còn lại, tôi có thể mời họ quay lại.

Hệ thống đặt chỗ không chỉ đơn thuần là nơi tiếp nhận đặt chỗ. Nó trở thành lối vào của mối quan hệ với khách. Ý tưởng này về sau dẫn đến hệ thống giảm giá và hệ thống chăm sóc khách quen.

Nhưng với một nền móng xây theo hứng nhất thời, về sau tôi đã phải trả một cái giá lớn. Tôi sẽ viết về điều đó ở Chương 2.

### 1-3 Xây dựng đợt tăng giá và giảm giá cùng một lúc

Với một nhà hàng hay quầy bar, tăng giá là quyết định không thể tránh. Nguyên liệu, điện nước và nhân công đều cứ đắt lên. Tamuro cũng đã tăng giá. Tôi tăng mỗi suất ăn theo set thêm khoảng ¥400–¥500 (khoảng $2,7–$3,3).

Mức tăng khá lớn, nên rõ ràng nếu cứ thế đưa ra thì khách quen sẽ rời đi. Vì vậy, đồng thời với việc tăng giá, tôi quyết định xây một hệ thống giảm giá vào hệ thống đặt chỗ. Nó không chỉ làm mọi thứ rẻ đi. Nó thưởng bằng giảm giá cho những khách có hành động tốt cho quán.

Thứ nhất là giảm giá theo nhóm. Càng đông người, giá mỗi người càng thấp. Khoảng một nửa số khách của Tamuro đến một mình, nhưng nếu họ đến theo nhóm thì doanh thu của quán tăng lên rất nhiều. Dù đã trừ đi phần giảm giá, quán vẫn có lợi. Với khách, đó cũng là lý do để rủ bạn bè. Thực tế, số khách đến theo nhóm nhờ ưu đãi theo số người trên trang đặt chỗ đã tăng lên.

Thứ hai là giảm giá đặt sớm. Đặt trước ít nhất một tuần được giảm 2%, trước ít nhất hai tuần được giảm 4%. Phần lớn lượt đặt chỗ ở Tamuro được thực hiện ngay trong ngày, nên tôi không thể đoán trước những gì sắp đến. Giảm giá đặt sớm là cơ chế để chốt doanh thu tương lai. Vào những ngày mưa và ngày lạnh, nếu đã có đặt chỗ, quán có thể chuẩn bị với tâm thế yên tâm.

Thứ ba, tôi cũng xây một cơ chế mua chung. Nếu một số người nhất định tụ họp vào một ngày giờ nhất định, một suất ăn set sẽ được cung cấp với giá giảm. Đáng lẽ đó là một cơ chế mang tinh thần Tamuro, nơi những người xa lạ tụ họp cùng một lúc.

Nhưng kế hoạch mua chung hoàn toàn không được dùng. Không có kết quả nào. Vào tháng 8 năm 2026, tôi dừng kế hoạch này và quyết định không dùng lại nữa.

Vứt bỏ thứ mình đã làm ra thì thấy tiếc. Nhưng nếu bạn xây bằng AI, chi phí và thời gian bỏ ra rất ít. Làm nhỏ, thử, và nếu không được thì bỏ đi. Tôi tin tốc độ này là lợi thế lớn nhất của việc vận hành một quán cùng AI.

Trong việc định giá còn một mẹo nữa. Trong các suất ăn, tôi cố ý đặt một suất cao cấp đắt tiền. Hầu như không ai chọn suất cao cấp cũng không sao. Có một suất đắt tiền bên cạnh, suất tiêu chuẩn trông có vẻ phải chăng. Nó đóng vai trò của cái gọi là điểm neo (một mốc tham chiếu để so sánh).

【Hình 1-7】Càng đông người, giá mỗi người càng thấp (so sánh 1, 4 và 6 khách)

### 1-4 Hệ thống chăm sóc khách quen

Khi tên và thông tin liên lạc đã còn lại trong hệ thống đặt chỗ, việc tiếp theo bạn muốn làm là vun đắp mối quan hệ với khách. Hệ thống quản lý thông tin khách hàng và làm sâu sắc thêm các mối quan hệ được gọi là CRM (quản lý quan hệ khách hàng). Từng chút một, tôi thêm các tính năng CRM vào hệ thống đặt chỗ của Tamuro.

Khi khách đăng ký làm hội viên, họ có thể xem lịch sử đặt chỗ trên một trang cá nhân. Nếu họ đăng ký ngày sinh, một ưu đãi sinh nhật sẽ được gửi đến. Hội viên đã lâu không ghé sẽ nhận được một tin nhắn mời quay lại. Cũng có một thẻ tích điểm bằng con dấu. Ghé ba lần được một ly đồ uống, năm lần được một suất bít tết và các ưu đãi khác, và sau khi đạt năm lần thì đếm lại từ đầu. Ngoài ra còn có tính năng giới thiệu bạn bè.

Tôi thiết kế cơ chế mời quay lại lần thứ hai với sự chăm chút đặc biệt. Người ta nói rằng ở nhà hàng và quầy bar, việc một khách mới có đến lần thứ hai hay không quyết định họ có trở thành khách quen hay không. Ở Tamuro, tôi gửi hai email mời ghé lại, vào ngày thứ bảy và ngày thứ 21 sau lần ghé đầu tiên. Email đầu không có phiếu giảm giá; chỉ email thứ hai mới có. Thay vì dụ người ta bằng giảm giá ngay từ đầu, trước hết tôi giúp họ nhớ lại. Nếu họ vẫn không đến, tôi mới thúc nhẹ một cái.

Tôi cũng chú ý để email không chồng chất lên nhau. Mỗi khách chỉ nhận tối đa một email mỗi ngày. Khi chúng trùng nhau, thứ tự ưu tiên là: sinh nhật, mời quay lại lần thứ hai, gọi hội viên đã lâu không ghé, các thông báo khác. Hội viên đã có lượt đặt chỗ tiếp theo sẽ không nhận email mời đến quán.

Việc đồng ý nhận email được để mặc định là tắt. Để bật sẵn thì số người nhận sẽ tăng, nhưng một thiết kế khiến người ta đồng ý mà không biết có thể trở thành vấn đề theo luật bảo vệ người tiêu dùng. Tôi chọn lấy sự tin tưởng thay vì con số. Đó là phán đoán của tôi.

Trong các email còn một nét nhỏ khác. Một mục "Chủ đề hôm nay" được đưa vào email xác nhận đặt chỗ. Đó là điều gì đó về mùa, về rượu vang hay về món ăn. AI tự động viết một chủ đề ngắn mỗi ngày.

Mục đích là trao cho khách một chủ đề mở đầu câu chuyện trước khi họ ghé quán. Tamuro là một quán có nhiều chuyện trò giữa các khách. Một chủ đề đọc được trong email trở thành điều đầu tiên họ nói với người ngồi bên cạnh ở quầy. Vì vậy tôi không để email xác nhận chỉ dừng ở "Đặt chỗ của bạn đã được tiếp nhận", mà làm cho nó chuyển trước đến khách một chút không khí của quán.

Tôi đã đổi AI viết các chủ đề một lần. Tôi chuyển sang một AI tạo ra những chủ đề tự nhiên hơn và gần với giọng điệu của quán hơn. Tuy nhiên, đây không phải cơ chế để tăng số khách. Đó là cơ chế để trải nghiệm của khách đến quán tốt hơn một chút. Tôi sẽ viết lại về sự phân biệt đó ở nửa sau của chương này.

Trong các cơ chế này, cái bắt đầu dần cho thấy kết quả là các suất "Rất vui được gặp" và "Chào mừng quay lại". Đây là những suất dễ chọn, giá hợp lý, chỉ khách lần đầu và khách đã hơn một năm chưa ghé mới được chọn. Chúng cho cả khách mới lẫn khách đang dần rời xa một lý do để đến.

Mặt khác, cũng có một vấn đề. Nhiều khách đặt chỗ với tư cách khách vãng lai mà không đăng ký làm hội viên. Nếu tôi đòi đăng ký hội viên ở mỗi lần đặt chỗ, họ có thể bỏ cuộc không đặt nữa. Vì vậy, sau khi đặt xong, tôi hiện một lời nhắc: "Bạn có muốn liên kết lượt đặt chỗ này với một tài khoản hội viên không?", và xây một cách để trở thành hội viên sau đó. Nó không dựng thêm rào cản nào cho việc đặt chỗ, mà gắn kết mối quan hệ về sau.

【Hình 1-8】Các suất chỉ khách lần đầu và người đã hơn một năm chưa ghé mới được chọn *(Màn hình hiển thị bằng tiếng Nhật.)*

【Hình 1-9】Thẻ tích điểm trên trang cá nhân (dữ liệu tổng hợp) *(Màn hình hiển thị bằng tiếng Nhật.)*

【Hình 1-5】Email xác nhận đặt chỗ. Có kèm một mục "Chủ đề hôm nay" (dữ liệu tổng hợp) *(Màn hình hiển thị bằng tiếng Nhật.)*

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

1. Trước hết, quyết định yêu cầu thật chi tiết. Xây cái gì, không xây cái gì, ai sẽ dùng. Hành vi của từng màn hình. Cách xử lý các trường hợp ngoại lệ (lỗi, bấm hai lần, hết hạn). Những quy tắc về sau dễ mâu thuẫn với nhau, như giá và giảm giá, tôi quyết định đặc biệt kỹ. Phần việc này tôi cũng làm qua đối thoại với AI trò chuyện. Tôi nhờ AI tìm trước các lỗ hổng và mâu thuẫn, còn chủ quán là người quyết định.
2. Ghi những gì đã quyết thành một "tài liệu yêu cầu". Không phải lời nói miệng hay chỉ thị tại chỗ, mà gom lại trong một tài liệu duy nhất. Đây là tiêu chuẩn duy nhất để sau này kiểm tra điều gì là đúng.
3. Giao cả tài liệu cho AI để nó triển khai. Tôi đưa toàn bộ tài liệu cho AI viết chương trình (Claude Code), kèm điều kiện đạt (mọi bài kiểm thử đều qua, kiểm tra ở môi trường thử trước khi lên bản chính thức, v.v.). AI tự xây cho đến khi đạt điều kiện và tự kiểm tra. Chủ quán chỉ xem khi nó dừng giữa chừng và ở bước kiểm tra cuối.

Ví dụ, tài liệu yêu cầu của cửa sổ trò chuyện "T-AI-MURO" đã được viết lại từ bản đầu tiên đến bản thứ ba. Ở bản thứ hai, tôi quyết định "không để AI tính giá", "gộp kiến thức của quán và việc tính giá vào một cửa sổ" và "vẫn giữ cả biểu mẫu, cho những người không muốn đặt chỗ qua trò chuyện". Ở bản thứ ba, tôi quyết định "bản gốc của kiến thức về quán được giữ ở đâu", "chỉ riêng cửa sổ này hiển thị các chỗ còn trống", "biến lượt trao đổi đầu tiên thành một câu hỏi bốn lựa chọn" và "không lưu nhật ký trò chuyện, chỉ lưu những câu hỏi chưa trả lời được". Nhờ các quyết định còn lại trong tài liệu, về sau tôi có thể lần ra vì sao mọi thứ lại như vậy.

Với cách xây dựng này, ngay cả khi thêm tính năng, tôi cũng nhận ra mâu thuẫn ngay bằng cách đối chiếu với tài liệu. Chính trong thời đại AI làm phần xây dựng, "năng lực ra quyết định" trước khi xây mới là thứ cần có. Đó là bài học lớn nhất tôi rút ra từ hệ thống đặt chỗ.

Tôi cũng đã xây một cơ chế đưa chính quy trình thành tài liệu rồi giao cho AI, để cách xây dựng này được chạy giống nhau mỗi lần tôi ra mắt một sản phẩm mới. Tôi sẽ viết về điều đó ở Chương 4.

【Hình 2-4】Mục lục của tài liệu yêu cầu T-AI-MURO (phiên bản 3) *(Màn hình hiển thị bằng tiếng Nhật.)*

### 2-6 Học ngôn ngữ của UI

Còn một điều nữa tôi phải học lại: tên của các thành phần trên màn hình.

Dù tôi đã bảo AI "làm thế này ở chỗ này", màn hình làm ra thường không như tôi mong. Khi nghĩ về nguyên nhân, tôi nhận ra mình không biết tên của các thành phần màn hình. Dù tôi có mô tả "một cửa sổ nhỏ hiện lên phía trên" hay "một thông báo biến mất sau vài giây", AI cũng khó hiểu tôi muốn nói gì.

Vì vậy tôi đọc một cuốn sách tham khảo về UI (giao diện người dùng, tức hình thức và cách thao tác của màn hình) và học tên của các thành phần cùng các thuật ngữ thiết kế.

| Thành phần | Là gì |
| --- | --- |
| Modal | Một cửa sổ nhỏ hiện lên phía trên màn hình. Bạn không thể thao tác màn hình phía sau cho đến khi đóng nó |
| Toast | Một thông báo hiện ở mép màn hình trong vài giây rồi tự biến mất |
| Tab | Cơ chế bấm vào một tiêu đề để chuyển nội dung |
| Accordion | Cơ chế bấm vào một tiêu đề để mở và đóng nội dung |
| Drawer | Một menu trượt ra từ cạnh màn hình như một ngăn kéo |
| Khác | Breadcrumb (dòng chỉ đường cho biết bạn đang ở đâu), carousel (các mục cuộn ngang), bottom sheet (bảng trượt lên từ đáy màn hình), v.v. Học thêm được tên nào là bạn chỉ dẫn được cho AI chỉ bằng một cụm từ |

Khi bạn trao đổi bằng tên gọi, màn hình do AI tạo ra sẽ gần đúng ngay từ lần đầu. Nếu bạn nói "Hiển thị màn hình xác nhận đặt chỗ dưới dạng modal", AI không phải lưỡng lự.

#### AI dễ ngả về hai thái cực giữa thêm và bớt

Ngay cả sau khi đã học được các từ này, việc xây màn hình cùng AI vẫn có một loại khó khăn khác. AI dao động rất mạnh.

Khi tôi nhờ làm phần đầu trang "sành điệu" cho trang đặt chỗ, tôi nhận được một phần đầu trang ấn tượng và dày. Nhưng mục đích của một trang đặt chỗ chỉ là đặt chỗ. Với khách quen thường xuyên đặt chỗ, một phần đầu trang dày với những lời giải thích dài chỉ là phiền. Tôi bảo AI cắt chiều dọc đi khoảng một nửa mà vẫn giữ nguyên lượng thông tin.

Khi tôi thống nhất phần chân của email và thêm một liên kết đến Sổ quán tiếp theo, phần nội dung chính bỗng trông đơn điệu và sơ sài so với nó. Vì vậy tôi thêm vào phần nội dung chính cả một tiêu đề, một bảng các điểm chính và một nút để bấm. Khi tôi thêm lối vào cửa sổ trò chuyện ở phần chân, trông nó rối mắt. Khi tôi nén nó thành hai dòng liên kết ngăn cách bằng đường kẻ, nó gọn gàng nhưng khó thấy. Cuối cùng nó ổn định ở hai thẻ cho thấy vai trò theo "khi nào dùng". Bên trái là "cho lần đặt chỗ tiếp theo của bạn", bên phải là "sau bữa ăn".

Quá dày, quá gọn, quá nổi bật. Điều quyết định chỗ vừa vặn mỗi lần là lời của chủ quán.

#### Một đề xuất thiết kế không có hình

Chuyện này cũng đã xảy ra. Tôi nhờ AI viết chương trình tạo các đề xuất cải thiện cho cửa sổ trò chuyện bằng một AI thiết kế (Claude Design), và một báo cáo quay về nói rằng "tôi đã làm đề xuất cho tám màn hình". Nhưng khi mở ra, chỉ có phần mô tả bằng chữ. AI đã không vẽ được hình, vậy mà chỉ còn lại báo cáo "xong rồi".

Cuối cùng, AI phía trò chuyện đã vẽ trực tiếp bốn đề xuất trong màn hình thiết kế. Nó lấy màu của màn hình hiện tại từ ảnh chụp màn hình, đặt lịch sử của quán vào một dòng thời gian, chia phần nêm nếm thành hai khung "cách nấu" và "vị", biến các gói thành thẻ giải thích, và thống nhất giá thành một bản tóm tắt đặt chỗ.

Khi bạn nhờ AI chạy kiểm thử, nó nói "đã qua". Khi bạn nhờ AI thiết kế, nó nói "xong rồi". Kiểm tra bên trong có gì là việc của con người. Tiêu chuẩn đánh giá là thứ con người buộc phải luôn nắm giữ.

#### Điều bạn có thể mang về từ chương này

- Xây được thứ chạy được và vận hành nó một cách an toàn là hai chuyện khác nhau.
- Hãy kiểm tra kết quả của AI không bằng lời của AI mà bằng kiểm thử. Một bài kiểm thử chỉ đáng tin khi bạn đã kiểm tra rằng nó sẽ thất bại lúc bạn cố tình làm hỏng chương trình.
- Những phép tính không được sai, như giá, đừng để cho việc sinh văn bản của AI. Hãy giao cho chương trình.

Phần tiếp theo của chương này (những lỗ hổng mới phát hiện và các bước tôi đã làm để vá) có trên note và X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Chương 3: Chia sẻ công cụ của quán tôi cho các quán khác

### 3-1 Tấm biển xanh nhỏ trên trang đặt chỗ

Mở trang đặt chỗ của Tamuro và bạn sẽ thấy một tấm biển xanh nhỏ ở gần phía trên. Khi quán đang mở, nó ghi "OPEN", và khi quán đóng, nó ghi "CLOSED". Khi chủ quán bấm nút kéo dài, giờ đóng cửa lùi lại 30 phút và tấm biển xuất hiện một chút sắc đỏ son.

Các quán ăn độc lập đều có một điểm chung. Họ mở cửa gần như đúng giờ, nhưng giờ đóng cửa thường bị trễ. Nếu cuộc trò chuyện với khách sôi nổi, đèn quán vẫn sáng quá giờ gọi món cuối lúc 10 giờ 30 tối.

Nhưng từ phía khách, bạn không thể thấy điều đó. Hiển thị "Đang mở cửa" trên Google Maps chỉ được xác định dựa trên giờ đã đăng ký, nên nó không phản ánh việc kéo dài, đóng sớm hay đóng cửa tạm thời. Không ai cất công đến một quán đã quá giờ đóng cửa mà nghĩ "Biết đâu quán vẫn còn mở". Gọi điện để hỏi cũng thấy ngại.

Tấm biển này là công cụ trả lời câu hỏi "Quán còn mở không?" đó. Nó được gọi là "AgendaLuce (Sổ tay ánh đèn)". Luce nghĩa là "ánh sáng" trong tiếng Ý.

Sổ tay ánh đèn được xây để chạy gần như không cần chủ quán để ý. Đăng ký giờ mở và đóng cửa cho từng ngày trong tuần một lần, tấm biển sẽ tự bật và tắt. Chủ quán chỉ chạm vào khi kéo dài, đóng sớm hoặc nghỉ một ngày. Để kéo dài, bạn bấm một nút trên điện thoại thông minh. Nhân viên cũng có thể thao tác từ một liên kết riêng không cần đăng nhập.

Khách không cần đăng nhập hay đăng ký. Mở trang công khai là bạn thấy trạng thái hiện tại của ánh đèn. Nếu thêm nó vào màn hình chính của điện thoại thông minh, nó hoạt động như một ứng dụng. Thành phần biển nhỏ này cũng có thể được nhúng vào các trang web khác. Thứ xuất hiện trên trang đặt chỗ của Tamuro chính là thành phần đó.

Sổ tay ánh đèn miễn phí. Nếu bạn chỉ nhúng thành phần biển vào trang web của mình, việc thiết lập mất khoảng 10 phút.

Và đây là điểm quan trọng. Sổ tay ánh đèn này không chỉ dành cho Tamuro. Quán nào cũng dùng được.

Tôi cố ý không đưa tên quán vào thiết kế của tấm biển. Nếu đặt tên lên đó, nó sẽ thành biển hiệu của Tamuro. Bạn cũng có thể chọn ngôn ngữ hiển thị. Tôi làm thành phần này nhỏ để nhúng được vào trang web của bất kỳ quán nào.

Một công cụ sinh ra từ vấn đề "giờ đóng cửa bị trễ" của Tamuro, ngay từ đầu được làm ở dạng ai cũng dùng được. Đó là Sổ tay ánh đèn. Và tập hợp những công cụ như thế chính là "loạt Agenda".

【Hình 3-1a】Tấm biển Sổ tay ánh đèn ở đầu trang đặt chỗ (đang mở) *(Màn hình hiển thị bằng tiếng Nhật.)*

【Hình 3-1b】Một chút sắc đỏ son xuất hiện khi đang kéo dài giờ *(Màn hình hiển thị bằng tiếng Nhật.)*

【Hình 3-6a】Màn hình của chủ quán. Để kéo dài, bấm nút một lần *(Màn hình hiển thị bằng tiếng Nhật.)*

【Hình 3-6b】Ngay sau khi bấm kéo dài. Giờ đóng cửa lùi lại 30 phút *(Màn hình hiển thị bằng tiếng Nhật.)*

【Hình 3-6c】Trang công khai mà khách nhìn thấy (trong lúc kéo dài) *(Màn hình hiển thị bằng tiếng Nhật.)*

### 3-2 Mọi chuyện bắt đầu từ cuốn sổ da đen

Loạt Agenda không được lên kế hoạch thành một loạt. Nó bắt đầu từ một hệ thống duy nhất, một hệ thống thậm chí còn chưa được phát hành.

Điều tôi định xây đầu tiên là một cơ chế nhận diện khuôn mặt khách và chào đón khách quen. Một chiếc camera ở lối vào quán phân biệt khách bằng khuôn mặt và báo cho chủ quán: "Đó là người đã ăn tonteki lần trước, người mà ba tháng rồi mình chưa gặp." Tôi định để một cỗ máy giúp làm công việc mà chủ một quán nhỏ vẫn làm trong đầu: nhớ khuôn mặt, tên và sở thích.

Nhưng ngay sau khi bắt đầu xây, tôi nhận ra đây là một hệ thống được giao phó một thứ rất nặng. Khuôn mặt. Thuộc tính. Lịch sử ghé quán. Tính cách của khách. Tất cả đều là thông tin một khi bị lộ thì không bao giờ lấy lại được.

Điều hiện lên trong đầu tôi lúc đó là "Cuốn sổ da đen" của Seicho Matsumoto. Một bản ghi không cho ai xem, nhưng chắc chắn tồn tại. Một cuốn sổ cái mà một khi mở ra có thể định đoạt cả sự sống chết của con người. Chẳng phải đó chính xác là thứ tôi đang cố xây sao?

Trong tiếng Ý, "sổ tay" là Agenda và "đen" là Nera. Ghép lại: AgendaNera. Cuốn sổ da đen. Tên gọi được quyết định đầu tiên như vậy.

AgendaNera vẫn đang được xây. Đây là sản phẩm tôi xây cẩn thận nhất trong loạt.

Và việc đặt tên này chính là bước ngoặt khởi đầu. Nếu có một cuốn sổ đen thì có thể có những cuốn sổ màu khác. Tôi sẽ xây lại các cơ chế mình dùng mỗi ngày trong quán thành dạng quán nào cũng dùng được, và phát hành từng cuốn một. Đó là [loạt Agenda](https://bontallc.com/agenda?via=b2-vi-{{FMT}}).

### 3-3 Thêm từng cuốn sổ một

Loạt Agenda là một tập hợp các ứng dụng web nhỏ, mỗi ứng dụng giải quyết một vấn đề của quán ăn bằng một công cụ. Mỗi cái có một cái tên tiếng Ý và một biệt danh tiếng Nhật kết thúc bằng "sổ". Mỗi cái tên có nguồn gốc riêng.

| Tên | Biệt danh | Nguồn gốc của tên | Công dụng |
| --- | --- | --- | --- |
| AgendaTimbro | Sổ chấm công | Timbro nghĩa là "con dấu". Đó chính là việc chấm công | Ghi lại giờ vào ca và ra ca của nhân viên |
| AgendaOro | Sổ tính lãi | Oro nghĩa là "vàng". Cuốn sổ tiền bạc | Ước tính khả năng sinh lời khi mở quán hoặc thêm món mới (miễn phí) |
| AgendaBis | Sổ quán tiếp theo | Bis nghĩa là "bis". Tiếng "Bis!" khán giả hô lên ở buổi hòa nhạc | Dẫn khách đến điểm dừng chân tiếp theo gần đó (miễn phí) |
| AgendaQA | Sổ hỗ trợ | Qua nghĩa là "ở đây". Khi gặp rắc rối, hãy đến đây | Bàn hỗ trợ chung của loạt (miễn phí) |
| AgendaLuce | Sổ tay ánh đèn | Luce nghĩa là "ánh sáng" | Cho biết quán có đang mở cửa hay không (miễn phí) |
| AgendaRicetta | Sổ giá vốn | Ricetta nghĩa là "công thức" | Tính giá vốn và tỷ lệ giá vốn của một công thức (miễn phí) |
| AgendaNera | Sổ khách quen | Nera nghĩa là "đen". Cuốn sổ da đen | Chào đón khách quen bằng nhận diện khuôn mặt (đang xây dựng) |
| AgendaTurno | Sổ xếp ca | Turno trong tiếng Ý là "lượt" hay "ca làm việc" | Thu thập nguyện vọng ca làm của nhân viên và phát lịch do AI riêng của chủ quán lập ra (sắp ra mắt) |

Cuốn sổ nào hợp với loại quán nào? Sổ chấm công dành cho những quán có từ hai nhân viên trở lên đang quản lý giờ làm bằng giấy hoặc trong LINE *(ứng dụng nhắn tin phổ biến nhất ở Nhật)*. Sổ tính lãi dành cho người sắp mở quán, và cho những ai muốn xem lại các con số vì tiền thuê hay chi phí đã thay đổi. Sổ quán tiếp theo dành cho những quán lấy bữa ăn làm trung tâm và muốn sớm đưa khách sang điểm dừng chân tiếp theo. Sổ tay ánh đèn dành cho các quán độc lập có giờ đóng cửa muộn hơn hoặc sớm hơn dự kiến. Sổ giá vốn dành cho những quán có công thức nằm trong đầu nhưng chưa bao giờ tính tỷ lệ giá vốn.

#### Sổ chấm công không tính lương

Sổ chấm công biến chiếc máy tính bảng của quán hoặc điện thoại thông minh của nhân viên thành máy chấm công ngay lập tức. Chỉ cần chạm vào tên của bạn. Bảng chấm công được tổng hợp tự động và có thể xuất ra CSV (định dạng mở được bằng phần mềm bảng tính). Ngày làm việc bắt đầu lúc 5 giờ sáng, nên dù quán mở đến khuya, ngày cũng không bị nhảy sang ngày mới.

Nhưng Sổ chấm công này cố ý không tính lương.

Lương theo giờ, phụ cấp và ngày chốt sổ khác nhau quá nhiều giữa các quán. Làm đêm tăng 25%, ngày lễ là một loại riêng, tiền đi lại tính theo số tiền mỗi ngày. Dù xây thế nào, nó cũng sẽ không vừa với quán của ai đó.

Vì vậy, thay vì tính toán, tôi chuẩn bị "một mẫu chỉ dẫn để đưa cho AI". Chủ quán dán tệp CSV chấm công đã tải về cùng mẫu này, nguyên như vậy, vào AI mà họ vẫn dùng thường ngày, dù là ChatGPT, Claude hay Gemini. Sau đó AI tính phụ cấp làm đêm, tiền làm ngày lễ và tiền đi lại rồi liệt kê ra. Quy tắc riêng của từng quán, như "chúng tôi chốt sổ vào cuối tháng, làm đêm tăng 25%, và Chủ nhật là một loại riêng", có thể được thêm vào mẫu và sẽ được phản ánh nguyên như vậy. Tệp CSV có các cột ngày trong tuần và tên ngày lễ để AI có thể tính đúng.

Tôi không nắm giữ cơ chế tính toán; mỗi quán tự giữ quy tắc của mình trong tay mình. Tôi nghĩ đó là cách khó hỏng nhất.

#### Dẫn khách đến điểm dừng chân tiếp theo, và để quán mình ở lại trong trí nhớ họ

Sổ quán tiếp theo là công cụ để làm "trang hướng dẫn điểm dừng chân tiếp theo" đưa cho khách. Với những khách đã ăn xong, nó dẫn họ đến một quán rượu gần đó hoặc nơi ăn nhẹ cuối buổi, kèm theo số phút đi bộ.

Nghe như một công cụ để tiễn khách đi nơi khác, nhưng bên trong có một mẹo nhỏ. Dẫn ai đó đến điểm dừng chân thứ hai có nghĩa là điểm dừng đầu tiên là quán của bạn. Trong khi có vẻ như tiễn khách đi, nó thực ra đang khắc vào trí nhớ họ rằng "điểm dừng đầu tiên là quán này". Nó được thiết kế như vậy.

#### Ba nguyên tắc thiết kế: tự động, mượn sức, đơn chức năng

Tất cả các cuốn sổ trong loạt Agenda đều có chung ba nguyên tắc.

Nguyên tắc thứ nhất là "tự động". Nó phải chạy mà chủ quán không cần chạm vào mỗi ngày. Với Sổ tay ánh đèn, một khi đã đăng ký lịch, ánh đèn tự bật và tắt. Chủ quán ăn không có thời gian chạm vào màn hình trong giờ phục vụ. Một công cụ không chạy nếu không chạm vào rồi cũng sẽ bị bỏ không.

Nguyên tắc thứ hai là "mượn sức". Đừng tự xây mọi thứ, hãy giao cho các công cụ và AI mà chủ quán đã dùng sẵn. Việc tính lương của Sổ chấm công là ví dụ điển hình. Sổ xếp ca cũng vậy: nó chỉ lo việc thu thập nguyện vọng của nhân viên, còn việc lập ca thì giao cho AI riêng của chủ quán. Nó không mang theo cơ chế phức tạp của riêng mình, cũng không mang chi phí gọi AI. Vì thế giá có thể giữ ở mức thấp.

Nguyên tắc thứ ba là "đơn chức năng". Mỗi cuốn sổ chỉ làm một việc, và làm chắc chắn. Một hệ thống đa chức năng quá nặng đối với một quán độc lập. Cứ thêm tính năng thì càng khó dùng, và mâu thuẫn về phía người xây cũng nhân lên. Đó là điều tôi tự mình học được qua hệ thống đặt chỗ ở Chương 2. Vì vậy tôi thêm từng cuốn sổ một, mỗi cuốn làm "đúng một việc này cho tử tế".

#### Vì sao hệ thống đặt chỗ không nằm trong loạt

Đến đây, tôi đoán sẽ có một câu hỏi hiển nhiên. Thứ Tamuro dồn nhiều công sức nhất là hệ thống đặt chỗ. Sao không đưa nó vào loạt Agenda?

Thực ra, tôi từng định làm vậy. Kế hoạch là đưa hệ thống đặt chỗ vào một dạng mà các quán ăn khác dùng được, và phát hành như một cuốn sổ của loạt. Nhưng vào tháng 8/2026, tôi đã hủy kế hoạch đó.

Lý do chính là điều tôi đã viết ở Chương 1. Hệ thống đặt chỗ của Tamuro chứa đầy cách kinh doanh của Tamuro. Rằng khách đi một mình chiếm một nửa lượng khách. Rằng gần 90% lượt đặt chỗ được thực hiện ngay trong ngày. Rằng tôi muốn bán khoảng thời gian trước giờ mở cửa. Rằng tôi muốn mọi người đến theo nhóm. Rằng tôi muốn nuôi dưỡng khách quen. Tôi xây các tổ hợp giảm giá, thứ tự các email và cách trò chuyện gợi ý đều để vừa với những điều này.

Nếu tôi làm loãng nó thành thứ ai cũng dùng được, nó sẽ thành một hệ thống đặt chỗ bình thường, quán nào cũng vừa vừa. Khi đó thế mạnh của Tamuro sẽ biến mất. Hệ thống đặt chỗ và CRM là cách quán tự bán mình. Thay vì ép quán vào một hệ thống chung, hãy làm hệ thống của quán vừa với quán. Quán của mình, theo đặc tả của mình. Vậy nên tôi quyết định giữ hệ thống đặt chỗ của Tamuro chỉ cho riêng Tamuro.

Vậy chẳng lẽ không có thứ gì để chia sẻ ra bên ngoài quán sao? Không. Quanh hệ thống đặt chỗ có nhiều vấn đề nhỏ chung cho mọi quán. Hãy giữ phần cốt lõi của quán theo đặc tả của riêng mình. Hãy xây các công cụ giải quyết những vấn đề xung quanh ở dạng ai cũng dùng được ngay từ đầu, và cho đi. Trang đặt chỗ của Tamuro là một bản mẫu có cả hai xếp trên cùng một màn hình. Trên một hệ thống đặt chỗ chỉ dành cho Tamuro có tấm biển Sổ tay ánh đèn mà ai cũng dùng được.

【Hình 3-2】Trang giới thiệu loạt Agenda *(Màn hình hiển thị bằng tiếng Nhật.)*

【Hình 3-3a】Giới thiệu Sổ chấm công *(Màn hình hiển thị bằng tiếng Nhật.)*

【Hình 3-3b】Giới thiệu Sổ tính lãi *(Màn hình hiển thị bằng tiếng Nhật.)*

【Hình 3-3c】Giới thiệu Sổ quán tiếp theo *(Màn hình hiển thị bằng tiếng Nhật.)*

【Hình 3-4】Màn hình chấm công của Sổ chấm công. Chỉ cần chạm vào tên của bạn (dữ liệu tổng hợp) *(Màn hình hiển thị bằng tiếng Nhật.)*

### 3-4 Xây cho mọi người ngay từ đầu

Tôi làm một công cụ cho quán của mình, rồi cũng chia sẻ cho các quán khác. Nói ra nghe đơn giản, nhưng để làm được, cách bạn quyết định mọi thứ trước khi bắt đầu xây phải thay đổi.

Nếu chỉ xây cho Tamuro, cách nhanh nhất là viết thẳng giờ mở cửa và tên của Tamuro vào chương trình. Nhưng khi đó không quán nào khác dùng được. Nếu về sau mới cố làm cho nó dùng chung, bạn sẽ phải đi tìm từng chỗ bị gắn cứng và sửa từng chỗ một.

Vì vậy các công cụ của loạt Agenda được đặc tả ngay từ đầu với tiền đề là ai cũng dùng được. Tôi bắt đầu từ một vấn đề ở Tamuro, nhưng ở giai đoạn yêu cầu, tôi tách thành hai câu hỏi: "Điều này chỉ đúng với Tamuro, hay đúng với mọi quán?" Đừng đặt tên quán lên biển. Để người dùng chọn ngôn ngữ. Làm cho nó dán được vào bất kỳ trang web nào. Tôi chốt những quyết định như vậy trong lúc viết tài liệu yêu cầu cho Sổ tay ánh đèn.

Đây là một công dụng nữa của việc xác định yêu cầu mà tôi đã học lại ở Chương 2. Nếu bạn quyết định những điều này trước, bạn có thể dùng công cụ ở Tamuro và chia sẻ nguyên như vậy cho các quán khác.

Vấn đề ở quán tôi cũng là vấn đề ở các quán khác. Không chỉ mình tôi là chủ quán muốn báo cho khách biết giờ đóng cửa đang bị trễ. Chủ một quán độc lập dựng một công cụ từ chính vấn đề của mình, rồi chia sẻ cho các quán khác. Đó là ý tưởng đằng sau loạt Agenda.

### 3-5 Dân chủ hóa công nghệ

Loạt Agenda hiện có hơn 10 sản phẩm. Tôi xây và vận hành chúng một mình, trong lúc đứng sau quầy bar.

Vài năm trước, điều này không thể tưởng tượng nổi. Để xây một sản phẩm, bạn cần người lập kế hoạch, người thiết kế màn hình, người viết mã, người kiểm thử và người vận hành. Không có đội ngũ và vốn, bạn không thể đưa một sản phẩm ra đời.

Điều đó không còn đúng nữa. Chủ quán nói yêu cầu cho AI, AI viết mã, AI kiểm thử, và một AI khác kiểm toán. Việc của chủ quán là quyết định xây gì, đánh giá kết quả của AI có hợp với mục đích của quán không, và chỉ làm những thao tác mà riêng con người mới làm được.

Kiểu thay đổi này thường được gọi là "dân chủ hóa công nghệ". Sức mạnh xây dựng không còn là tài sản của một số ít người hay công ty.

Nhưng hãy để tôi thành thật ở đây. Như tôi đã viết trong Lời mở đầu, tôi làm trong ngành CNTT khoảng 16 năm, chủ yếu ở mảng lập kế hoạch hệ thống và làm cầu nối giữa những người trực tiếp làm nghiệp vụ với các đơn vị phát triển phần mềm. Tôi biết cách xác định yêu cầu, cách nghĩ về cơ sở dữ liệu và cách chạy kiểm thử, tất cả đều từ kinh nghiệm. Vì vậy tôi sẽ không nói rằng một người chưa từng viết một dòng mã nào cũng có thể làm điều tương tự bắt đầu từ ngày mai.

Dù vậy, rất nhiều thứ đã thay đổi. Giờ đây tôi có thể tự mình xây, trong những khoảng trống của công việc chính, những thứ ở quy mô mà trước kia cần cả một đội. Và với những người chưa có kinh nghiệm, cánh cửa vào chắc chắn đã thấp hơn. AI sẽ dạy bạn nếu bạn hỏi về điều bạn không hiểu. Nó sẽ cho hình hài những gì bạn nói bằng lời. Cái thiếu không phải là kỹ thuật mà là khả năng quyết định xây gì và những từ ngữ để nói với AI. Đó là những khả năng mà người điều hành quán vẫn dùng mỗi ngày.

### 3-6 Cuộc tranh luận về "cái chết của SaaS"

Phần mềm mà người ta dùng qua internet và trả phí hằng tháng, như loạt Agenda, được gọi là SaaS (Software as a Service, phần mềm như một dịch vụ). Phần mềm kế toán, quản lý giờ làm và chấm công, quản lý đặt chỗ. Các quán ăn ngày nay vận hành trên rất nhiều SaaS.

Liệu AI có chấm dứt SaaS không? Năm 2026, cuộc tranh luận đó bùng lên dữ dội.

Một ngòi nổ là phát biểu của CEO Microsoft Satya Nadella. Trên một podcast vào tháng 12/2024, Nadella nói rằng các ứng dụng SaaS sẽ sụp đổ trong thời đại các tác tử AI. Lập luận là: một khi các tác tử AI đảm nhận phần ra quyết định của công việc kinh doanh, phần mềm được xây để con người thao tác qua màn hình sẽ không còn cần thiết.

Rồi vào tháng 2/2026, Anthropic công bố Claude Cowork (một công cụ AI tự thực hiện các công việc kinh doanh), và cổ phiếu của các công ty phần mềm Mỹ bị bán tháo mạnh. Ở Phố Wall, cú lao dốc này được gọi là "SaaSpocalypse". Điều nhà đầu tư lo sợ là nếu các tác tử AI làm việc, mô hình SaaS thu phí theo từng người (định giá theo từng ghế) sẽ sụp đổ.

Cũng có những phản biện. CEO Nvidia Jensen Huang nói rằng các tác tử AI sẽ không thay thế phần mềm mà sẽ dùng phần mềm thay con người, và gọi đợt bán tháo là phản ứng thái quá. Không ít người khác cũng cho rằng SaaS biết hấp thụ AI thì ngược lại còn mạnh lên.

SaaS có thực sự chết không? Đây là điều tôi nghĩ.

Cái sẽ chết là tầng giữa của SaaS: loại thu phí hằng tháng cao theo từng tài khoản (per seat) và giả định rằng con người thao tác nó qua màn hình. Nếu AI làm việc thay con người, bạn không cần trả phí theo từng tài khoản người dùng. Nếu không ai thao tác màn hình, bạn không cần một màn hình cầu kỳ.

Cái còn lại là những công cụ rẻ và làm một việc cho chắc chắn. Và những công cụ mà AI dễ dùng.

Đây chính là ba nguyên tắc của loạt Agenda. Nó chạy tự động, nó được giao cho AI của chủ quán (dựa vào lực bên ngoài), và nó chỉ làm một việc (đơn chức năng). AgendaTurno giao việc lập lịch ca cho AI của chủ quán, đúng là hình thức "AI dùng phần mềm" mà Huang mô tả. Hệ thống đặt chỗ của Tamuro mở một ô cửa qua MCP cho AI của khách, và đó cũng là cùng một ý tưởng.

Tất nhiên, ở đây có vẻ như có một mâu thuẫn. Tôi nói về cái chết của SaaS, vậy mà loạt Agenda tự nó cũng là SaaS. Nhưng loạt Agenda là một bộ công cụ do một chủ quán xây cho quán của mình rồi công khai với giá thấp. Nó không phải mô hình thu phí hằng tháng cao theo từng tài khoản (per seat), và cũng không giả định rằng mọi người ngồi dán mắt vào màn hình mỗi ngày. Nó được xây ngay từ đầu trên tiền đề rằng AI sẽ dùng nó.

#### "Cái chết của SaaS" đối với các quán ăn

Cuộc tranh luận này nghe có thể như chuyện của nhà đầu tư và ngành CNTT. Nhưng với các quán ăn, điều tương tự sắp xảy ra dưới một hình thức quen thuộc hơn nhiều.

Nhiều quán độc lập trả phí hằng tháng cho các trang ẩm thực và trang đặt chỗ, và ngoài ra còn trả hoa hồng giới thiệu cho mỗi lượt đặt chỗ. Đổi lại việc đưa khách đến, trang web nắm giữ mối liên hệ với khách, và chuyện quán không có cả thông tin liên lạc của khách cũng không hiếm. Nếu giá tăng, quán không có lựa chọn nào khác ngoài đi theo, và nếu hệ thống xếp hạng thay đổi, dòng khách cũng thay đổi.

Như tôi đã viết ở Chương 1, năm 2026 là lúc kỷ nguyên bắt đầu, khi khách có AI riêng của mình tìm quán. Nếu lối vào chuyển sang AI, toàn bộ cục diện trả phí hằng tháng và hoa hồng cho một trang web để được xếp cao trong danh sách của nó bắt đầu lung lay. Nếu một quán tự mở ô cửa cho AI, khách có thể đến được quán mà không qua các trang lớn. Hồ sơ đặt chỗ và mối quan hệ với khách vẫn nằm trong tay quán.

Nếu nói "cái chết của SaaS" bằng lời của một quán độc lập, thì đó là "sự kết thúc của thời trả tiền là được lên danh sách". Tamuro đã mở ô cửa của mình qua MCP, và giữ hệ thống đặt chỗ cùng CRM theo đặc tả của riêng mình, như một sự chuẩn bị cho điều đó.

SaaS có chết hay không, hiện chưa ai biết. Nhưng hình dạng của những công cụ sẽ còn lại trong thời đại AI đang dần hiện ra. Đó là điều tôi nghĩ.

### 3-7 Kiếm tiền: nhỏ, nhiều, rẻ

Tôi xây loạt Agenda với mục tiêu để nó đứng vững như một việc kinh doanh. Mục tiêu là biến nó thành trụ cột thu nhập thứ hai, tách khỏi quán ăn.

Tôi đặt giá nhỏ và thấp. Phí hằng tháng bắt đầu từ vài trăm yên. Chẳng hạn Sổ chấm công là ¥500 (khoảng $3,3) mỗi tháng. Tôi cũng xen vào những công cụ miễn phí, như Sổ tính lãi, Sổ tay ánh đèn và Sổ giá vốn. Các công cụ miễn phí đóng vai trò lối vào để mọi người biết đến loạt Agenda. Sổ tay ánh đèn không dùng API bản đồ lẫn AI tạo sinh, nên chi phí vận hành gần như bằng không. Vì thế tôi có thể tặng miễn phí.

Chỉ có một tài khoản. Với một tài khoản chung gọi là AgendaID, bạn dùng được mọi công cụ trong loạt. Bạn không cần đăng ký lại cho từng công cụ. Các công cụ trả phí có ba tháng miễn phí và có thể bắt đầu mà không cần đăng ký thẻ. Thời gian miễn phí chỉ có một lần cho mỗi tổ hợp quán và sản phẩm. Nếu bạn giới thiệu một quán khác, bạn nhận được phần thưởng.

Lý do tôi giữ được giá thấp nằm ở cách xây. Tôi xây một mình, tôi nhờ AI xây, và tôi tái sử dụng một nền tảng chung. Chi phí cơ sở dữ liệu được giữ ở khoảng $35 mỗi tháng cho cả loạt. Nếu cả chi phí xây lẫn chi phí vận hành đều nhỏ, một việc kinh doanh có thể đứng vững ngay cả với doanh thu nhỏ.

Hãy để tôi nói thật. Vào lúc tôi viết cuốn sách này, một số quán đã thử các công cụ, nhưng hầu như chưa có đăng ký trả phí nào. Hệ thống để xây đã sẵn sàng, còn hệ thống để được biết đến vẫn ở phía trước. Cuốn sách này cũng là một phương tiện phục vụ mục đích "được biết đến" đó.

#### Xây một thứ và giữ cho người ta tiếp tục dùng là hai chuyện khác nhau

Hãy để tôi nói thật thêm một điều. Xây được một công cụ và có người tiếp tục dùng nó là hai việc riêng biệt.

Việc xây đã nhanh hơn nhờ AI. Nhưng để người ta tiếp tục dùng thì cần những việc khác. Trả lời các câu hỏi về cách dùng (Sổ hỗ trợ sinh ra để làm việc này). Gửi thông báo trước khi hết thời gian miễn phí. Giải thích lý do khi tăng giá. Xóa dữ liệu cho đúng cách khi ai đó yêu cầu hủy. Và trên hết, giữ cho nó chạy mà chủ quán không cần chạm vào.

Trong ba nguyên tắc của loạt Agenda, "tự động" là nguyên tắc cho việc "giữ họ tiếp tục dùng" này. Một công cụ không chạy nếu chủ quán không chạm vào mỗi ngày rồi cũng sẽ bị hủy. Xây xong chưa phải là xong. Nó chỉ trở thành một việc kinh doanh khi nó tiếp tục được dùng. Thêm từng quán tiếp tục dùng, từng quán một: đó là việc của tôi sau khi xuất bản cuốn sách này.

#### Nếu bạn muốn bắt đầu ở quán của mình

Với những ai đọc cuốn sách này và muốn thử ở quán của mình, có ba bước.

1. Mở https://bontallc.com/agenda?via=b2-vi-{{FMT}} và đăng nhập bằng tài khoản Google (AgendaID sẽ được tạo. Không cần đăng ký thẻ)
2. Trước hết, thêm một cuốn sổ miễn phí. Tôi khuyên dùng Sổ tay ánh đèn. Bạn chỉ cần chèn tiện ích bảng hiệu vào trang web của mình, và nó chạy trong 10 phút. Nếu bạn chưa mở quán, hãy thử Sổ tính lãi
3. Nếu thấy hợp, hãy thử Sổ chấm công miễn phí trong ba tháng. Thông báo sẽ đến khi gần hết hạn, nên bạn sẽ không bị tính phí dù để mặc đó

Nếu có thắc mắc, hãy hỏi qua Sổ hỗ trợ (AgendaQA). AI trả lời ngay các thắc mắc về thao tác, còn các câu hỏi về đặc tả và lỗi thì tôi tự đọc.

Doanh thu của một quán ăn phụ thuộc vào thời tiết và mùa. Số chỗ ngồi và giờ mở cửa đều có giới hạn. Còn doanh thu từ công cụ thì không có giới hạn về chỗ ngồi. Vừa điều hành quán vừa chia sẻ những công cụ sinh ra từ vấn đề của chính quán mình, và để điều đó chậm rãi thành thu nhập: tôi tin đây có thể trở thành một cách kiếm tiền khác cho một quán độc lập.

#### Vẫn là công ty nhỏ, nhưng vươn ra thế giới

Còn một điều nữa tôi đã quyết định về loạt Agenda ngay từ đầu. Tôi sẽ không xây nó chỉ bằng tiếng Nhật.

Sổ chấm công, Sổ tính lãi và Sổ hỗ trợ đều dùng được bằng 20 ngôn ngữ. Chữ trên màn hình và các câu hỏi thường gặp, tất cả. Một công cụ được xây cho một quán bar 19 chỗ ngồi ở Tokyo hoạt động y như vậy bằng tiếng Anh, tiếng Hàn, tiếng Việt.

Có hai lý do. Một là vấn đề của các quán ăn không đổi khi đổi quốc gia. Bạn muốn ghi lại lúc nhân viên đến và đi. Bạn muốn biết khả năng sinh lời trước khi mở quán. Bạn muốn báo cho khách biết giờ đóng cửa đã được kéo dài. Đây đều là những vấn đề mà các quán độc lập trên khắp thế giới cùng có. Lý do còn lại là số quán độc lập ở Nhật cứ giảm dần. Nếu tôi chỉ phục vụ thị trường tiếng Nhật, doanh số công cụ sẽ có trần.

Trước đây, để một công ty nhỏ bán sản phẩm ra nước ngoài, nó cần đại lý địa phương, công ty dịch thuật và pháp nhân. Giờ AI hỗ trợ việc dịch và hiệu đính. Các hệ thống thanh toán chung hoạt động trên khắp thế giới. Để giao hàng chỉ cần một máy chủ, và không có hàng tồn hay nhà kho ở từng nước. Một công cụ do một chủ quán làm ra có thể nằm trên kệ của thế giới bằng 20 ngôn ngữ vào ngày hôm sau khi nó được làm xong. Trước đây, chỉ các công ty lớn mới làm được điều đó.

Một công ty rất nhỏ làm ăn với nhiều nước ngay từ đầu: những công ty như vậy đôi khi được gọi là micro-multinational (công ty đa quốc gia siêu nhỏ). Bonta LLC nhắm đúng đến điều đó, với một quán ở Higashi-Nakano và một chủ quán.

Tất nhiên, dịch sang 20 ngôn ngữ không có nghĩa là các chủ quán ở nước ngoài sẽ bắt đầu dùng ngay. Một số bản dịch vẫn đang chờ người bản ngữ rà soát để nghe tự nhiên. Dù vậy, nhờ gỡ bỏ rào cản ngôn ngữ ngay từ đầu, trần về mức độ các công cụ có thể vươn tới sẽ biến mất, giống như trần về số chỗ ngồi.

Tôi đang xây nền tảng đó như thế nào là câu chuyện của Chương 4.

【Hình 3-5】Chuyển đổi ngôn ngữ trong Sổ hỗ trợ. 20 ngôn ngữ được liệt kê *(Màn hình hiển thị bằng tiếng Nhật.)*

## Chương 4: Công nghệ - Hệ thống để liên tục xây sản phẩm một mình

Những điểm chính của chương này

- Tôi biến quy trình ra mắt một sản phẩm mới thành tài liệu, ở dạng (một kỹ năng) mà AI đọc và thực hiện được. Việc của con người chỉ là phán đoán và những thao tác chỉ con người mới làm được
- Các phần dùng chung, như đăng nhập, thanh toán, trang giới thiệu và hướng dẫn sang các sản phẩm khác, được xây một lần và tái sử dụng cho mọi sản phẩm. Chi phí cơ sở dữ liệu của nền tảng đó khoảng $35 mỗi tháng
- Hệ thống vẫn đang được nuôi lớn. Tôi liên tục bổ sung vào tài liệu quy trình những thất bại, như một bản thiết kế bị từ chối năm lần liên tiếp

(Đây là chương có nhiều thuật ngữ kỹ thuật. Nếu bạn không quan tâm đến công nghệ, bạn có thể nhảy sang Chương 5 và câu chuyện vẫn liền mạch.)

### 4-1 ProductBootstrap: giao chính quy trình ra mắt cho AI

Mỗi lần xây một sản phẩm, tôi lại lặp lại cùng những bước chuẩn bị và cùng những sai lầm. Tạo một repository (kho chứa chương trình). Kết nối đăng nhập. Quyết định màu thiết kế. Dựng hệ thống kiểm thử. Chuẩn bị môi trường chính thức. Chắc chắn tôi đã làm hết ở sản phẩm trước, nhưng tôi quên các chi tiết và vấp ở cùng những chỗ.

Vì vậy tôi biến quy trình ra mắt một sản phẩm mới thành tài liệu. Dạng của nó mà AI viết mã (Claude Code) đọc và thực hiện được là cái tôi gọi là một "kỹ năng" (skill). Tên của kỹ năng này là ProductBootstrap. "Bootstrap" là thuật ngữ phổ biến trong thế giới máy tính, chỉ việc tự khởi động từ một cơ chế tối thiểu, và tôi áp dụng nó vào việc ra mắt sản phẩm.

Tôi không giữ chương trình mẫu nào. Tôi sao chép sản phẩm hoàn thành gần nhất và bắt đầu sản phẩm mới từ đó. Như vậy, những bài học mới nhất tự động được truyền sang sản phẩm tiếp theo. Cũng không cần phải tiếp tục bảo trì một mẫu cũ.

#### Luồng của quy trình

1. Giao tài liệu yêu cầu. Nếu các trường bắt buộc (tên sản phẩm, công dụng, người dùng, giá, đơn vị tính giá, màu nhận diện, vị trí của bản thiết kế gốc, v.v.) còn để trống, AI không bắt đầu. Quy tắc là nó không hỏi chủ quán giữa chừng. Nếu ngay từ đầu mọi thứ chưa đủ, nó không bắt đầu
2. Quyết định màu của sản phẩm. Mỗi sản phẩm trong loạt Agenda có một màu nhận diện. AI đo màu của các sản phẩm hiện có, đề xuất khoảng bốn ứng viên không trùng nhau, và chủ quán chọn
3. Chốt thiết kế. Tôi nhờ một AI thiết kế (Claude Design) tạo các đề xuất cho các màn hình. AI tự kiểm tra tối đa ba vòng, và chỉ các đề xuất qua được bước kiểm tra mới được cho chủ quán xem
4. Giao phần triển khai cho AI làm đến cùng. AI tự xây và tự sửa cho đến khi đạt các điều kiện nghiệm thu đã đặt (kiểm tra kiểu, kiểm tra phong cách mã, mọi bài kiểm thử đều xanh, qua mọi bước kiểm tra màn hình, và các thay đổi cơ sở dữ liệu chạy suôn sẻ ở môi trường thử)
5. Chủ quán chỉ phê duyệt khi lên bản chính thức. Mọi thứ cho đến môi trường thử diễn ra không cần người giám sát, và chủ quán chỉ phán đoán thao tác lên bản chính thức

Tôi xây giai đoạn triển khai sao cho nó không dừng giữa chừng để chờ chủ quán phê duyệt. Những ngày đầu, tôi tiến hành bằng cách xin phê duyệt ở từng giai đoạn, nhưng như vậy thì chẳng có gì tiến lên. Khi có nhiều cửa sổ làm việc của AI, mỗi cửa sổ dừng lại chờ phê duyệt, và chủ quán phải đi vòng qua từng cửa sổ để phán đoán. Vì vậy tôi đã đổi: tôi giao trước phạm vi đã được duyệt và các điều kiện nghiệm thu mà máy có thể đánh giá, và nó chỉ dừng khi thất bại.

Các điều kiện dừng cũng được đặt ra. Khi tài liệu quy trình và phán quyết của chủ quán xung đột. Khi cần một thao tác chỉ con người mới làm được. Khi nó không tiến triển được trên cùng một lỗi ba lần liên tiếp. Khi xác thực hết hạn, quyền không đủ, hoặc cần một thao tác không thể hoàn tác. Ngoài ra, AI tự tiến hành. Trạng thái công việc được ghi trong một tệp nhỏ, nên dù nó sập giữa chừng, nó vẫn tiếp tục được từ đó.

#### Con người chỉ làm hai việc

Tôi đã viết điều này trong tài liệu quy trình: AI thực hiện mọi bước. Chủ quán chỉ có thể được nhờ hai việc sau.

- Chính việc phán đoán. Phê duyệt, phán quyết, quyết định chọn một trong hai phương án
- Những thao tác chỉ con người mới làm được. Các khóa chỉ cấp được từ màn hình quản trị của một dịch vụ bên ngoài, các đơn đăng ký có xác minh danh tính, thao tác trên thiết bị thật và đánh giá bằng mắt

Nếu AI giao bất cứ việc nào khác cho chủ quán, đó là vi phạm tài liệu quy trình. Trong bảng quy trình, tôi thêm một cột "người thực hiện" vào mỗi dòng, và dòng nào mà mục của chủ quán không nêu được lý do thì bị chuyển sang phía AI.

Tôi có lý do để đặt ra quy tắc này. Khi tôi sắp xếp công việc còn lại của một sản phẩm, AI xếp "tạo dự án máy chủ", "đăng ký đích đăng nhập", "nhập các biến môi trường" và "dựng môi trường thử" đều là việc của chủ quán. Mỗi việc đều là thao tác mà AI tự thực hiện được. "Sao mình lại là người làm việc này?" là phản ứng thật lòng của tôi lúc đó. AI tự làm nếu bạn nhờ. Nhưng nếu bạn không nhờ, nó chuyển cho con người. Vì thế tôi phải ghi nó vào tài liệu quy trình.

Tôi đã đưa mọi thất bại của hệ thống đặt chỗ mà tôi mô tả ở Chương 2 vào danh sách kiểm tra của tài liệu quy trình này. Đưa kiểm thử vào trước. Đừng giữ dữ liệu chính thức trong môi trường phát triển. Dựng môi trường thử trước. Sản phẩm tiếp theo tránh được cùng nỗi đau ngay từ đầu.

#### Vẫn đang lớn lên

Tài liệu quy trình này không phải một sản phẩm đã hoàn chỉnh. Đó là thứ tôi liên tục bổ sung mỗi khi có điều gì thất bại.

Chẳng hạn, có lần tôi nhờ AI thiết kế tạo màn hình cho một sản phẩm năm lần liên tiếp, và cả năm đều bị từ chối. Trong đó có cả những vòng tôi đã đưa cho nó các quy tắc thiết kế chung của cả loạt (DESIGN.md).

Ban đầu, AI chẩn đoán nguyên nhân là "chính bảng màu". Tôi bác bỏ điều đó. Nguyên nhân thực sự là hai điều. Một là những màu không có định nghĩa trong quy tắc được dùng tùy ý. Hai là ba phần có vai trò khác nhau được xếp chồng theo chiều dọc với cùng màu nền và cùng lề, không có ranh giới giữa chúng. Không quy tắc nào bị vi phạm, vậy mà các vai trò đã biến mất khỏi vẻ ngoài.

Vì vậy tôi thêm các điều khoản vào quy tắc thiết kế. Đừng cho những thứ có vai trò khác nhau cùng một diện mạo. Đừng chỉ phân tách bằng màu. Thứ quan trọng nhất đứng đầu trong đường nhìn. Chỉ những thứ thật sự ngang nhau mới được xếp cùng độ nặng. Đừng làm bố cục chỉ xếp chồng theo chiều dọc.

Còn một bài học nữa từ thất bại. Nếu bạn chỉ truyền đạt "diện mạo mặc định cần tránh" dưới dạng danh sách cấm, AI sẽ lắc hẳn sang một mặc định khác không có trong danh sách. Khi tôi cấm cùng lúc thẻ, bóng đổ và góc bo tròn, thứ quay về là một màn hình giống tờ báo chỉ gồm đường kẻ và lề. Từ đó, tôi cho viết tài liệu yêu cầu thành ba cột: "kiểu mẫu cần tránh", "điều tôi muốn cấm" và "thay vào đó làm gì".

Tôi cũng đổi giữa chừng cách quyết định màu nhận diện. Khoảng khi số sản phẩm vượt quá tám, dải màu đậm đã bị các sản phẩm hiện có lấp đầy, và từ sản phẩm thứ chín trở đi không thể có màu đậm cho đường kẻ và nút bấm mà không va chạm với các sản phẩm hiện có. Vì vậy tôi sửa quy tắc: màu nhận diện của sản phẩm chỉ dùng cho màu bề mặt nhạt, còn đường kẻ, đường viền, biểu tượng và nút chính đều thống nhất theo màu mực chung của loạt. Đó là một ràng buộc chỉ lộ rõ khi các sản phẩm đã nhiều lên.

Mỗi khi có điều gì thất bại, tôi sửa tài liệu quy trình. Sản phẩm tiếp theo nhờ vậy dễ hơn một chút. Tôi tin việc nuôi lớn tài liệu quy trình là khoản đầu tư tốt nhất để tiếp tục xây sản phẩm một mình.

【Hình 4-2】Các giai đoạn của quy trình ra mắt, và ai thực hiện chúng (AI hay chủ quán) *(Màn hình hiển thị bằng tiếng Nhật.)*

【Hình 4-3】Các màu nhận diện của loạt Agenda. Mỗi sản phẩm một màu, chỉ dùng trên bề mặt *(Màn hình hiển thị bằng tiếng Nhật.)*

### 4-2 AgendaHub: cửa chính

Khi sản phẩm nhiều lên, bạn cứ phải xây đi xây lại cùng những thứ. Đăng nhập, thanh toán, trang giới thiệu, hướng dẫn sang các sản phẩm khác. Để vận hành một mình, bạn cần xây các phần dùng chung một lần và tái sử dụng cho mọi sản phẩm.

AgendaHub là nơi các phần dùng chung đó được gom lại. Tôi gọi nó là "cửa chính".

Trước hết, nó là lối vào định tuyến từ một địa chỉ đến mọi sản phẩm. Dưới một tên miền duy nhất, bontallc.com, lối vào cho từng sản phẩm được xếp thành hàng: /agendatimbro, /agendaoro, /agendaluce. Với khách, trông như thể các sản phẩm nằm trong một trang, nhưng thực ra phía sau mỗi cái là một chương trình riêng đang chạy.

Tiếp theo, đó là nơi đặt các trang giới thiệu sản phẩm. Có một trang giới thiệu cho cả loạt, và trong đó có một mục cho từng sản phẩm. Mỗi mục có tên sản phẩm và biệt danh, giá, một vấn đề được nêu bằng lời của chính chủ quán bắt đầu bằng "Khi bạn...", phần mô tả những gì nó làm được, và một liên kết đến trang chi tiết. Khi tôi phát hành một sản phẩm mới, việc thêm mục này nằm trong quy trình ra mắt.

Và đó là nơi chứa các quy tắc thiết kế và quy trình ra mắt. Bản gốc của các màu nhận diện, các quy tắc màn hình (DESIGN.md), kỹ năng ProductBootstrap tôi đã mô tả ở 4-1, kỹ năng kiểm tra màn hình, và kỹ năng thực hiện thay đổi cơ sở dữ liệu một cách an toàn. Với mọi quy tắc xuyên suốt cả loạt, nội dung thật nằm ở đây, và mỗi sản phẩm đọc nó bằng cách tham chiếu.

【Hình 4-1】Cấu trúc của loạt Agenda. Từ cửa chính (AgendaHub) đến từng cuốn sổ, và mọi cuốn sổ đều kết nối với một tài khoản (AgendaID) *(Màn hình hiển thị bằng tiếng Nhật.)*

### 4-3 AgendaID: tài khoản và thanh toán dùng chung

AgendaID là hệ thống dùng chung của loạt cho tài khoản và thanh toán.

Một chủ quán đăng nhập một lần bằng tài khoản Google là dùng được mọi sản phẩm. Không cần tạo tài khoản cho từng sản phẩm. Tôi cũng dự định sau này sẽ mang cài đặt ngôn ngữ xuyên qua các sản phẩm.

Thanh toán cũng là một hệ thống duy nhất. Thay vì xây kết nối đến dịch vụ thanh toán (Stripe) cho từng sản phẩm, AgendaID gánh hết. Có bốn hạng mục giá: sản phẩm nhẹ ¥300 (khoảng $2) mỗi tháng, sản phẩm trả theo mức dùng, sản phẩm mua một lần ¥600 (khoảng $4), và sản phẩm miễn phí. Các sản phẩm trả phí có ba tháng miễn phí không cần đăng ký thẻ, dùng được một lần cho mỗi tổ hợp quán và sản phẩm. Cũng có một cơ chế cộng thêm ba tháng miễn phí cho cả người giới thiệu lẫn người được giới thiệu.

Trước khi hết thời gian miễn phí, email thông báo đến trước bảy ngày và một ngày. Lúc đầu tôi cũng xây các email này bên trong Sổ chấm công, nhưng khi sản phẩm nhiều lên, tôi nhận ra việc cho mọi sản phẩm cùng một cơ chế là lãng phí, nên tôi gom nó về phía AgendaID.

#### Hủy dịch vụ và xóa dữ liệu cũng theo quy tắc chung

Có một phần giản dị nhưng quan trọng: hủy dịch vụ và xóa dữ liệu.

Khi một khách hàng hủy, dữ liệu nào bị xóa, và khi nào? Nếu bạn xây riêng cho từng sản phẩm, chắc chắn sẽ sót ở đâu đó. Hơn nữa, loạt Agenda có những sản phẩm xử lý dữ liệu đặc biệt nhạy cảm, như sản phẩm nhận diện khách quen bằng khuôn mặt.

Vì vậy tôi chia mức độ chi tiết của việc xóa thành bốn cấp và biến nó thành quy tắc dùng chung cho cả loạt. Đó là hủy một sản phẩm, xóa một quán, rút tài khoản (rời cả loạt), và yêu cầu xóa từ một nhân viên cá nhân. Các cấp trên kéo theo các cấp dưới, và mỗi sản phẩm đăng ký quy trình xóa dữ liệu của riêng mình với hệ thống chung. Thời gian ân hạn cho việc xóa là 30 ngày, và trong thời gian đó có thể hoàn tác.

Kèm theo đó là một trục thời gian. Chẳng hạn, bảng chấm công theo luật phải được lưu giữ năm năm. Dù một nhân viên cũ yêu cầu xóa, trong thời hạn lưu giữ thì hồ sơ phải được giữ lại, với tên và các thông tin tương tự được ẩn danh, chứ không xóa vật lý. Tôi cần quyết định ranh giới giữa "xóa" và "giữ" bằng cách đối chiếu với luật.

#### Một đăng nhập thử để AI không làm nhiễm bẩn bản chính thức

Tôi thêm vào AgendaID một cơ chế nữa, dành cho AI: một lối vào đăng nhập thử.

Để AI kiểm tra mọi thứ chạy được, AI phải đăng nhập và thao tác các màn hình. Nhưng đăng nhập được thực hiện bằng tài khoản Google, nên AI không tự đăng nhập được. Và tôi cũng không thể giao tài khoản của chủ quán cho AI. Có nguy cơ các bài kiểm thử của AI làm nhiễm bẩn dữ liệu chính thức.

Vì vậy tôi xây một lối vào cấp các tài khoản tổng hợp (persona) chỉ dùng được ở môi trường thử. Nó không hoạt động ở bản chính thức. Cơ sở dữ liệu của môi trường thử là một dự án tách biệt với bản chính thức và chỉ chứa dữ liệu tổng hợp. AI đăng nhập qua lối vào này, thao tác các màn hình và xác nhận mọi thứ chạy được. Các tài khoản thử được dựng lại mỗi ngày, và tài khoản cũ bị xóa.

Nhờ vậy, AI có thể tự thực hiện cả bước kiểm tra cuối, trong một môi trường dựng giống hệt bản chính thức, mà không chạm vào bản chính thức.

### 4-4 Điều hướng chung, và thất bại của từ "cửa chính"

Để người dùng đi được từ bất kỳ sản phẩm nào sang các sản phẩm khác, tôi cho mọi sản phẩm một menu điều hướng chung. Đó là con đường giúp một chủ quán bar đang dùng Sổ chấm công đặt câu hỏi ở Sổ hỗ trợ, hoặc đi xem các cuốn sổ khác.

Đằng sau điều hướng chung này có một câu chuyện thất bại nhỏ.

Ở phiên bản đầu tiên, tôi đặt một liên kết ghi "Quay lại cửa chính". Đó là vì trong nội bộ, tôi gọi AgendaHub là "cửa chính". Nhưng khi kiểm tra trên thiết bị thật, có gì đó không ổn. Hai liên kết "Quay lại cửa chính" và "Xem loạt Agenda" nhảy đến cùng một chỗ. Hơn nữa, liên kết hỗ trợ nằm phía trên menu công việc hằng ngày, nên thứ tự quan trọng bị ngược. Và trên hết, từ "cửa chính" chẳng có nghĩa gì với một chủ quán lần đầu dùng sản phẩm. Đó là ngôn ngữ nội bộ của chính người làm ra nó.

Vì vậy tôi đặt lại các nguyên tắc. Sắp xếp các mục theo mức gần với mục đích của người dùng: công việc hằng ngày ở trên cùng, các liên kết dẫn ra ngoài ở dưới cùng. Ngay cả một liên kết nhằm thu hút người dùng mới cũng không bao giờ đứng trên công việc. Ranh giới phải giải thích được bằng một đường kẻ. Viết câu chữ bằng ngôn ngữ của người dùng, không phải ngôn ngữ nội bộ. Không bao giờ đặt nhiều hơn một liên kết nhảy đến cùng một chỗ. Tôi bỏ "Quay lại cửa chính" và gộp mọi thứ thành một liên kết duy nhất, "Xem các cuốn sổ Agenda khác".

Ở Chương 2, tôi đã viết về việc học ngôn ngữ của UI. Đó là ngôn ngữ để chủ quán dùng khi nói chuyện với AI. Đây là chiều ngược lại: ngôn ngữ mà người làm ra sản phẩm dùng để nói với người dùng. Ở cả hai trường hợp, đều là chuyện chỉnh lời nói của mình cho hợp với người mình đang nói chuyện.

【Hình 4-4】Điều hướng chung sau khi sửa. Công việc ở trên cùng, và các liên kết dẫn ra ngoài ở dưới cùng *(Màn hình hiển thị bằng tiếng Nhật.)*

### 4-5 Nền tảng tốn $35 mỗi tháng

Chi phí cơ sở dữ liệu của toàn bộ nền tảng được mô tả trong chương này là khoảng $35 mỗi tháng. Gói trả phí bao gồm dự án chính thức là $25, và dự án cho môi trường thử là $10.

Cái này cũng không phải con số từ đầu. Có lúc tôi trả $45 mỗi tháng. Cơ sở dữ liệu phát triển của một sản phẩm nhận diện khuôn mặt vẫn bị tính phí dù tôi không dùng. Tôi chuyển nó sang gói miễn phí và dừng nó, xóa một dự án khác tôi không dùng, và nhờ vậy xuống được mức hiện tại.

Tôi cũng để mắt đến chi phí của AI. Công việc của AI viết chương trình được tính phí theo lượng token (đơn vị văn bản mà AI đọc và viết). Tôi tránh để chi phí dồn lại bằng cách để cửa sổ làm việc giữ vai trò điều phối, và giao chính phần triển khai cho một AI khác có hạn mức chi phí riêng. Với mô hình tạo sinh trong cửa sổ trò chuyện cũng vậy, tôi xem giá và chọn cái cần thiết và đủ dùng. Ngay cả khi một mô hình hạng cao hơn chỉ tốn thêm $1 mỗi tháng, tôi chọn bằng cách hỏi "thế này đủ chưa?"

Nếu bạn xây nhỏ, ngay cả doanh thu nhỏ cũng nuôi được bạn. Câu chuyện kiếm tiền ở Chương 3 được nâng đỡ bởi việc chi phí của nền tảng này nhỏ đến mức nào.

### 4-6 AI điều phối, và người đưa ra quyết định

Cuối cùng, hãy để tôi mô tả hình dạng một ngày làm việc của tôi.

Tôi mở nhiều cửa sổ làm việc của AI cùng lúc. Có một cửa sổ cho hệ thống đặt chỗ, một cửa sổ cho mỗi sản phẩm, và một cửa sổ điều phối gửi chỉ thị cho chúng và gom kết quả. Tôi đặt tên cửa sổ điều phối là AgendaRegia (cuốn sổ điều phối).

Những người đưa ra phán quyết, tức quyết định "đi hướng nào", là tôi và AI phía trò chuyện. AI phía trò chuyện tìm trước các khoảng trống và mâu thuẫn trong đặc tả, gắn cho mỗi cái một phán quyết mặc định, và đề xuất tất cả cùng lúc. Tôi đọc và quyết định. Những gì đã quyết được gom vào một bản chỉ thị gọi là Goal và dán vào cửa sổ làm việc. Nó gồm các phê duyệt trước và các điều kiện đạt mà máy có thể đánh giá. Cửa sổ làm việc đọc nó và làm tiếp đến cùng, chỉ dừng khi có điều gì thất bại.

Tôi cũng cho bản chỉ thị kèm theo ước tính khi nào công việc xong. Tôi xếp công việc này vào giữa các khung giờ mở cửa của quán, nên nếu không biết một việc mất bao lâu thì tôi không lập được kế hoạch cho ngày của mình.

Vai trò của chủ quán không phải đọc mà là quyết định. Tôi không cần đọc toàn bộ 1.775 bản ghi trò chuyện. Tôi trả lời các câu hỏi về thông tin thực tế của quán. Tôi phán quyết những việc chỉ chính sách của quán mới quyết định được. Sau khi một thứ chạy thật, tôi tự chạm vào nó năm sáu lần để kiểm tra xem có gì thấy lạ không. Chỉ vậy thôi.

Trước khi đến được hình thức này, tôi đã làm lại công việc nhiều lần. AI tự thêm tính năng và các màn hình trở nên không ổn định. Công việc phình ra không giới hạn từ một chỉ thị duy nhất. Chờ phê duyệt ở từng giai đoạn thì chẳng có gì tiến lên. Mỗi lần như vậy, tôi thêm một quy tắc, và đó là cách nó đến được hình thức hiện nay. Cái này cũng vẫn đang lớn lên.

#### Điều bạn có thể mang về từ chương này

- Với công việc lặp lại, hãy biến chính quy trình thành tài liệu và giao cho AI. Nếu mỗi lần thất bại bạn sửa tài liệu quy trình, lần sau sẽ dễ hơn
- Hãy xây các phần dùng chung (đăng nhập, thanh toán, điều hướng) chỉ một lần và tái sử dụng cho mọi sản phẩm. Nếu nền tảng nhỏ, ngay cả doanh thu nhỏ cũng nuôi được bạn
- Con người chỉ làm phần phán đoán và những thao tác chỉ con người mới làm được. Nếu AI giao bạn bất cứ việc nào khác, hãy thêm nó vào tài liệu quy trình

Phần tiếp theo của chương này (những cuốn sổ tiếp theo tôi sẽ xây, và những bài học tôi đã thêm vào tài liệu quy trình) có trên note và X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Chương 5: Tương lai của một quán bar nhỏ

### 5-1 Từ Zatta Gohan đến Tamuro

Tôi bước vào ngành ăn uống năm 39 tuổi.

Cơ duyên là một quán bar trong khu phố tên là Zatta. Mỗi tháng một lần, thỉnh thoảng hai tuần một lần, họ cho tôi phục vụ các bữa ăn ở đó. Tôi đã tự học nấu ăn từ lâu, nhưng khi đó tôi đã có một nơi để mọi người ăn món của tôi và vui vẻ. Đó là trải nghiệm ban đầu của tôi.

Năm 2014, tôi mở một quán ăn tên Zatta Gohan ở Arai-Yakushi. Đó là một quán nhỏ phục vụ cơm phần. Tôi điều hành nó bảy năm.

Tuy nhiên ở Arai-Yakushi, tôi cảm thấy có giới hạn về lượng khách. Rồi tôi tìm được một mặt bằng ở Higashi-Nakano. Đi bộ từ cửa ra phía đông của ga mất chưa đến một phút. Ngay cả ngày mưa, bạn cũng đến được mà không bị ướt nhiều.

Tháng 11/2018, tôi mở Tamuro ở đó. "Tamuro" nghĩa là nơi mọi người tụ họp. Quán có 11 chỗ ngồi ở quầy và 8 chỗ ngồi chiếu tatami, tổng cộng 19. Trong ba năm, tôi điều hành song song hai nơi, Arai-Yakushi và Higashi-Nakano. Trong thời kỳ COVID, việc giữ cả hai trở nên khó khăn, nên tôi đóng quán ở Arai-Yakushi và chỉ còn lại Tamuro.

#### Quán bar tuyển chọn

Tamuro tự gọi mình là "quán bar tuyển chọn" (curation bar).

Curation nghĩa là có con mắt tinh tường. Trước khi là đầu bếp, tôi muốn là một người tuyển chọn (curator). Món ăn, đồ uống, bầu không khí của quán: tôi làm tất cả bằng cách chọn lọc với một con mắt tinh tường. Đó là Tamuro.

Tôi thường đi du lịch để ăn, cả ở nước ngoài lẫn trong nước Nhật. Việt Nam, Campuchia, Ý, Thượng Hải, Bắc Kinh, Mexico. Đi ăn khắp nơi là một niềm vui, và đồng thời là cách tìm ra thứ để phục vụ ở Tamuro. Tôi tái tạo những nguyên liệu đắt tiền bằng nguyên liệu trong tầm tay. Chẳng hạn, nếu bạn phơi khô lòng đỏ trứng rồi bào ra, bạn được một hương vị gần với bottarga. Tôi coi kiểu thay thế này (địa phương hóa) là vai trò của mình.

Tôi đã học nấu ăn lại trong thời kỳ COVID. Tôi học một khóa nấu ăn Pháp gồm tổng cộng tám buổi, và cũng tham gia một khóa ẩm thực Nhật. Cách xử lý vị umami, và kỹ thuật kiểm soát lửa. Những gì tôi học ở đó là nền tảng cho cách nấu ăn của tôi ngày nay.

Thực đơn của Tamuro gồm bốn món khai vị và một món chính. Tôi cho nó nhiều loại nguyên liệu để khách sống một mình được ăn nhiều rau. Tôi sắp xếp sao cho các cách nấu (chiên, ngâm giấm, hầm, nướng) và các hương vị (ngọt, cay, chua) không trùng nhau. Món được ưa chuộng nhất là tonteki, bít tết heo. Nó có nước sốt hơi ngọt làm từ nước tương Kyushu, với thật nhiều tỏi.

#### Nơi mọi người tụ họp

Khoảng một nửa khách của Tamuro đến một mình. Họ chủ yếu ở độ tuổi 30 đến 50, và nhiều người là hàng xóm ở Higashi-Nakano, nhưng cũng có người đến từ vùng quanh Akabane, Shinjuku, Nishi-Ogikubo, Ogikubo và Eifukucho. 

Nét đặc trưng của quán là khách trò chuyện với nhau rất nhiều. Tôi làm quầy sao cho dễ nói chuyện với người ngồi bên cạnh, và tôi hoặc nhân viên quyết định chỗ ngồi bằng cách đánh giá ai sẽ hợp nhau. Khách đến một mình đôi khi về sau lại đến cùng nhau. Đúng như cái tên, nó đã thành nơi mọi người tụ họp. Tôi thường đăng những hoạt động thường ngày của quán trên [Instagram](https://www.instagram.com/tamuro.higashinakano/).

Trong bữa tối theo thực đơn cố định tổ chức khoảng mỗi tháng một lần, tôi phục vụ bảy đến tám món trong hai đến ba tiếng, cùng với rượu vang ghép món. Mỗi tháng chủ đề thay đổi: Ý, Pháp, Nhật. Các lớp nấu ăn là những buổi workshop ba tiếng, và sau khi nấu, mọi người cùng nâng ly, ăn rồi ra về. Có aperitivo, phục vụ rượu vang và món nhỏ vào đầu buổi tối trước giờ mở cửa. Có tiệc nướng barbecue khoảng hai lần mỗi năm. Có một buổi tất niên mỗi năm. Và có lễ hội yukata mà tôi đã viết ở Chương 1.

Hệ thống đặt chỗ tôi viết ở Chương 1, cửa sổ trò chuyện và MCP đều là công cụ để đưa mọi người đến quán này. AI là phương tiện để kết nối và thu hút mọi người, không phải mục tiêu.

### 5-2 Món cà ri hamburger của Quatre Épices

Tamuro là quán bar ban đêm. Ban ngày, không gian bỏ trống.

Tận dụng khoảng thời gian đó, tôi bắt đầu Quatre Épices vào tháng 1/2024. Đó là một quán cà ri hamburger chỉ hoạt động vào buổi trưa ở cùng địa điểm, và do nhân viên điều hành.

Quatre Épices nghĩa là "bốn loại gia vị" trong tiếng Pháp. Đúng như tên gọi, thay vì chồng thật nhiều gia vị lên nhau, chúng tôi chọn lọc và thu hẹp lại để làm rõ đường nét của hương vị. Món cà ri không dùng bột mì; nó được hoàn thiện bằng độ sánh tự nhiên của chính rau và thịt. Cảm giác thỏa mãn khi ăn xong, và dạ dày không nặng nề. Và sự hài hòa với hamburger. Tôi thiết kế nó dựa trên ba tiền đề đó.

Chúng tôi kỹ lưỡng trong cách nấu hamburger. Chúng tôi đặt tỷ lệ pha trộn để bên ngoài giòn, bên trong mềm xốp, và nấu sao cho hợp với tỷ lệ đó. Kỹ thuật kiểm soát lửa mà tôi học vào ban đêm ở Tamuro cũng được phát huy trong đĩa ăn ban ngày.

Giá cả, ngày và giờ kinh doanh có thể thay đổi, nên xin hãy xem Instagram của Tamuro (https://www.instagram.com/tamuro.higashinakano/) để biết thông tin mới nhất.

Quatre Épices còn điều hành một quán ăn cho trẻ em ở cùng địa điểm. Đó là một hoạt động tận dụng cơ sở vật chất và việc mua hàng sẵn có của quán bar để phục vụ bữa ăn cho trẻ em trong khu phố. Qua mối liên hệ đó, chúng tôi cũng xây dựng quan hệ với trung tâm cộng đồng địa phương. Đôi khi chúng tôi phục vụ cà ri và bánh sandwich tại các sự kiện thể thao địa phương, sự kiện của trung tâm cộng đồng và các lễ hội múa Bon.

Thành thật mà nói, việc tận dụng giờ ban ngày không phải tất cả đều suôn sẻ. Tôi đã tạo những ngày uống rượu ban ngày và cho người khác thuê không gian, nhưng khách không đến như tôi mong. Sức hấp dẫn của quán bar được cảm nhận khác nhau khi chủ quán có mặt vào ban đêm và khi chỉ có nhân viên ban ngày. Phát triển quán ban ngày với một sức hút khác với quán ban đêm vẫn là một nhiệm vụ chưa hoàn thành.

### 5-3 Bonta LLC: hai trụ cột

Công ty nhỏ điều hành Tamuro và Quatre Épices là Bonta LLC. Tôi là thành viên quản lý của công ty.

Công ty có hai trụ cột. Một là ăn uống: Tamuro và Quatre Épices. Hai là CNTT: phát triển loạt Agenda và tư vấn.

Ăn uống và công cụ khác nhau về cách kiếm tiền. Nâng đỡ công ty bằng hai trụ cột có bản chất khác nhau là hình thức tôi hình dung.

Và hai trụ cột cung cấp nguyên liệu cho nhau. Rắc rối ở quán bar trở thành hạt giống của một công cụ. Những gì tôi học được từ việc xây công cụ quay lại vào việc vận hành quán bar. Sổ tay ánh đèn sinh ra từ việc giờ đóng cửa bị trễ, và hồ sơ giờ kéo dài từ Sổ tay ánh đèn trở thành nền tảng cho các ước tính lợi nhuận và ca làm. Những "câu hỏi chúng tôi không trả lời được" tích lại trong cửa sổ trò chuyện cải thiện phần hướng dẫn của quán. Vòng tuần hoàn này là lý do tôi có thể tự mình quản lý cả quán bar lẫn việc phát triển.

Tôi không nghĩ đến việc làm công ty lớn hơn. Nhỏ, nhiều và rẻ. Đó là mô hình hoạt động của công ty này.

### 5-4 Viết với tư cách Raku Bonta

Khi viết và xuất bản, tôi dùng bút danh "Raku Bonta". Tôi cũng viết cuốn sách này dưới tên đó.

Cuốn sách trước của tôi, *Phó quản lý AI*, là sách về AI tạo sinh. Nó đứng đầu hạng mục quản lý thời gian của Amazon và được nhiều người đọc. Cuốn sách này là phần tiếp theo của nó.

Ngoài sách, tôi còn viết trên note. Tôi viết về những nỗ lực của quán bar với AI, những gì tôi tìm thấy trong một chuyến đi học hỏi, tiến độ xuất bản sách của tôi, và loạt Agenda. Bạn có thể theo dõi phần tiếp theo mà tôi không thể đưa vào cuốn sách này trên note (https://note.com/bontallc).

Với tôi, viết cũng là một cách để diễn đạt cả quán bar lẫn việc phát triển thành lời và kiểm tra chúng. Như tôi đã viết ở Chương 1, kiến thức đầu tiên của cửa sổ trò chuyện "T-AI-MURO" được xây từ những lời tôi vẫn để lại trên X. Những gì tôi viết ra đã trở thành nguyên liệu cho AI. Từ nay về sau, những gì tôi viết cũng sẽ quay lại cho cả quán bar lẫn AI.

Còn một điều nữa tôi đã quyết định về việc viết. Tôi không thông báo những thứ chưa hoàn thành bằng "sắp ra mắt". Tôi làm cho xong, làm một trang giới thiệu, và chỉ khi đó mới đưa ra. Tôi tin giữ đúng thứ tự đó là điều giúp một công ty nhỏ có được lòng tin.

### 5-5 Tương lai của quán độc lập

Cuối cùng, tôi sẽ gom những gì đã viết trong cuốn sách này thành một bức tranh duy nhất.

【Hình 5-1】Bức tranh tổng thể của những gì cuốn sách này mô tả. Một quán bar nhỏ tự mở ô cửa của mình (câu chuyện thứ nhất), và biến rắc rối của mình thành công cụ để trao cho các quán bar khác (câu chuyện thứ hai) *(Màn hình hiển thị bằng tiếng Nhật.)*

Khách sẽ dần để AI của riêng họ tìm quán bar và đặt chỗ. Tháng 8/2026, đã có thể đặt chỗ nhà hàng từ ChatGPT thông qua một dịch vụ đặt chỗ lớn. Lối vào đang chuyển từ các trang tìm kiếm và đánh giá ẩm thực sang AI của riêng mỗi người.

Khi đó, một quán bar không có tên trên dịch vụ đặt chỗ lớn sẽ vô hình với AI. Nhưng ngay cả khi bạn không ở trên dịch vụ lớn, vẫn có một con đường để quán bar kết nối trực tiếp với AI. Tamuro đã chọn con đường đó bằng cách mở một ô cửa gọi là MCP. Một quán bar nhỏ tự mình mở ô cửa của riêng mình. Đó là câu chuyện thứ nhất của cuốn sách này.

Chủ quán bar sẽ có thể biến rắc rối của chính mình thành công cụ và chia sẻ cho các quán bar khác. Sổ tay ánh đèn sinh ra từ rắc rối của Tamuro khi muốn báo cho mọi người biết giờ đóng cửa sẽ bị trễ, và quán bar nào cũng dùng được. Sức mạnh để xây dựng đang trở thành thứ không còn chỉ dành cho một số người hay công ty nhất định. Chủ một quán bar nhỏ chuyển từ phía dùng công cụ sang phía xây dựng và phân phối công cụ. Đó là câu chuyện thứ hai của cuốn sách này.

Điểm chung của hai câu chuyện này là quán bar càng nhỏ thì càng có thể sắc bén.

Các chuỗi lớn khái quát hóa hệ thống của mình để mọi cửa hàng đều mang lại cùng chất lượng. Tamuro thì ngược lại. Khách đi một mình chiếm một nửa, gần 90% lượt đặt chỗ được thực hiện ngay trong ngày, và khách trò chuyện với nhau. Để hợp với tính cách đó của Tamuro, tôi đã xây hệ thống đặt chỗ, các khoản giảm giá và cửa sổ trò chuyện một cách chi tiết. Vì không khái quát hóa nên nó sắc bén. Vì sắc bén nên nó trở thành lý do để khách chọn.

Và quán bar càng sắc bén thì càng tìm ra nhiều hạt giống của công cụ. Càng đối diện với tính cách của quán bar, rắc rối của bạn càng cụ thể. Rắc rối cụ thể trở thành công cụ cụ thể. Công cụ cụ thể giúp các quán bar khác có cùng rắc rối.

AI đã giúp một chủ quán làm được cả hai. Làm sắc bén quán bar, và chia sẻ công cụ. Trước đây, bạn phải chọn một trong hai. Giờ bạn làm được cả hai.

Tất nhiên, mọi thứ vẫn đang trong quá trình hoàn thiện. Tỷ lệ đạt của cửa sổ trò chuyện vẫn đang được nâng lên. Tài liệu quy trình được bổ sung sau mỗi thất bại. Cách phát triển quán ban ngày vẫn là một thách thức. Số người đặt chỗ qua AI vẫn chưa nhiều.

Dù vậy, tôi tin tương lai của quán bar nhỏ rất tươi sáng. Nhỏ không phải là điểm yếu. Vì nhỏ, chúng tôi thử nhanh, bỏ nhanh và sửa nhanh. Vì nhỏ, chúng tôi có thể sắc bén. Và rắc rối của một quán bar sắc bén trở thành công cụ và truyền sang các quán bar nhỏ khác.

Tôi đã viết cuốn sách này từ một quán bar 19 chỗ ngồi ở Higashi-Nakano.

## Lời kết

Cảm ơn bạn đã đọc đến đây.

Những gì tôi viết trong cuốn sách này là một bản ghi tính đến tháng 10/2026. Các công cụ AI thay đổi chỉ trong vài tháng. Một số cơ chế tôi mô tả có thể đã mang một hình dạng khác vào lúc cuốn sách này được xuất bản. Dù vậy, tôi vẫn viết ra, tin rằng bản ghi về việc một quán bar nhỏ đã xây gì với AI và xây bằng cách nào, đã thất bại ở đâu và rút ra điều gì, sẽ còn hữu ích trong một thời gian.

Loạt Agenda: https://bontallc.com/agenda?via=b2-vi-{{FMT}}

Theo dõi hoạt động của tôi: note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

Nếu có dịp đến Higashi-Nakano, hãy ghé Tamuro. Bạn có thể đặt chỗ qua trang đặt chỗ, qua cửa sổ trò chuyện "T-AI-MURO" trên trang đó, và tất nhiên là qua AI của chính bạn.

Trang đặt chỗ của Tamuro: https://tamuroreservation.vercel.app/?src=b2-vi-{{FMT}}

Instagram của Tamuro: https://www.instagram.com/tamuro.higashinakano/

Dành cho những ai muốn thử đặt chỗ từ AI. Địa chỉ kết nối của máy chủ MCP của Tamuro là URL sau.

https://tamuroreservation.vercel.app/api/mcp

Trong phần cài đặt của AI của bạn (như Claude hay ChatGPT), hãy mở màn hình thêm công cụ bên ngoài (connector, máy chủ MCP) và đăng ký URL này. Cách đăng ký khác nhau tùy AI và thay đổi theo thời gian, nên cách an toàn nhất là tra "MCP" hoặc "connector" trong phần trợ giúp của từng AI. Tùy gói bạn đang dùng, bạn có thể không kết nối được một máy chủ MCP do mình tự chọn. Sau khi đăng ký, hãy hỏi AI của bạn: "Tối nay Tamuro còn chỗ không?" Nó sẽ kiểm tra các chỗ trống và giá, rồi dẫn bạn đến trang đặt chỗ. Nút xác nhận do chính bạn bấm.

Dành cho những ai đến sau khi đọc sách. Khi đặt chỗ, xin hãy nhập mã phiếu giảm giá "BOOK". Chúng tôi sẽ mời bạn một ly cho vòng đầu tiên. Nếu bạn đến mà không đặt chỗ, chỉ cần nói "Tôi biết quán qua sách" khi gọi món đầu tiên. Chúng tôi sẽ phục vụ bạn cùng ly đồ uống đó. Đó là một mẹo nhỏ để tôi đếm được bao nhiêu người đến từ cuốn sách.

Bạn có thể vào quán mà không cần đặt chỗ. Dù đi một mình, bạn cũng sẽ không thấy lạc lõng. Thậm chí bạn có thể vui vẻ trò chuyện với người ngồi bên cạnh.

Tôi đang chờ bạn ở nơi mọi người tụ họp.

Raku Bonta

### Tài liệu tham khảo

- OpenAI Help Center, "ChatGPT — Release Notes," August 10, 2026, "Restaurant reservations in ChatGPT" https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- Alpaca, "Alpaca MCP Server" (một ví dụ về máy chủ MCP ở Mỹ cho phép AI đặt lệnh mua bán cổ phiếu và các chứng khoán khác) https://docs.alpaca.markets/docs/alpaca-mcp-server
- Cuộc tranh luận về "cái chết của SaaS": phát biểu của Satya Nadella trên podcast BG2 (tháng 12/2024), đợt lao dốc mạnh của cổ phiếu phần mềm vào tháng 2/2026 cùng tên gọi của nó, và lời phản bác của Jensen Huang được lấy từ các bài báo và bình luận sau. https://www.longangle.com/alts-education/software-ai  /  https://www.fastcompany.com/91504460/everything-youve-heard-about-the-saaspocalypse-is-wrong  /  https://en.thairath.co.th/money/tech\_innovation/tech\_companies/2916811
