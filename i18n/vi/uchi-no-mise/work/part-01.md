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

