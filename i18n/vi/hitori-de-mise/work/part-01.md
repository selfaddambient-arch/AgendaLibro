## Lời mở đầu

Cuốn sách này là bản ghi chép tính đến tháng 1 năm 2026. Từ đó đến nay, một số cách tôi vận hành quán, cũng như tên gọi và thông số của các công cụ AI, đã thay đổi. Phần tiếp theo, tôi đã viết trong cuốn thứ hai, *Làm riêng cho quán bar của mình*.

### Vì sao một người từng làm hệ thống lại trò chuyện với AI trong một quán ăn dưới tầng hầm

Cảm ơn bạn đã cầm cuốn sách này lên.

*Một người điều hành cả quán, và AI xuất hiện ngay bên cạnh tôi.*

Thấy tiêu đề ấy, có thể có bạn nghĩ: "Đúng là mình rồi." Cũng có bạn thắc mắc: "AI xuất hiện bên cạnh nghĩa là sao?"

Đây không phải sách kỹ thuật về lập trình khó nhằn. Đây là cuốn sách dành cho những người như bạn, những chủ quán ngày nào cũng đứng trong bếp, lo chuẩn bị nguyên liệu và lúc nào cũng bận rộn với khách.

Trước hết xin giới thiệu đôi chút về tôi.

Hiện nay tôi điều hành một quán ăn nhỏ ở tầng hầm của một tòa nhà tại Higashi-Nakano *(một khu dân cư ở phía tây Tokyo, ngay phía tây Shinjuku)*, Tokyo.

Quán mang hai diện mạo khác nhau. Ban ngày, đó là quán chuyên cà ri thịt viên kiểu hamburger thơm mùi gia vị. Ban đêm, đó là quán bar ăn uống phục vụ set ăn đổi món theo ngày và đồ uống.

▼ Cà ri hamburger Quatre Epice (Instagram)

https://www.instagram.com/quatre.epice.hamburg.curry/

![Cà ri hamburger Quatre Epice (Instagram)](images/fig-01.png)

▼ Quán bar "Tamuro" (Instagram)

https://www.instagram.com/tamuro.higashinakano/

![Quán bar "Tamuro" (Instagram)](images/fig-02.png)

Đó là một không gian ấm cúng, chỉ có 11 chỗ ngồi ở quầy và 8 chỗ trên bục tatami.

Nhưng quán không chỉ phục vụ món ăn.

Cứ hai tuần một lần, tôi tổ chức sự kiện rượu vang, và mỗi tháng một lần lên kế hoạch cho một lớp học nấu ăn hoặc một ngày thực đơn đặc biệt. Dù chỉ là một tầng hầm chật chội, ngày nào tôi cũng tất bật không ngơi tay.

Năm nay là năm thứ mười hai tôi điều hành quán.

Trước đó, tôi là nhân viên công ty. Công việc của tôi là "lập kế hoạch hệ thống" và "kiến trúc giải pháp".

Nghe vậy, đôi khi người ta đáp: "Vậy là bạn từng phát triển những hệ thống ghê gớm nhỉ." Thực ra không phải thế.

Việc tôi làm không phải là viết mã chương trình khó. Tôi lắng nghe điều những người làm việc trực tiếp mong muốn, truyền đạt chính xác cho các nhà cung cấp IT (công ty phát triển) và nhờ họ xây dựng. Tôi là một "người điều phối". Ở Nhật, vị trí này thường được gọi là "dân làm hệ thống".

Nhân viên làm việc trực tiếp ao ước: "Ước gì công việc của mình nhẹ nhàng hơn." Còn các kỹ sư thì nói: "Chúng tôi cần các yêu cầu được định nghĩa một cách logic."

Việc của tôi là đứng giữa hai bên, thông dịch ngôn ngữ của mỗi bên và dẫn mọi người đến đích.

Vì thế tôi hiểu những bất tiện và nỗi lo của những người như bạn, những người dùng hệ thống, và tôi cũng hiểu phần nào bên IT đang nghĩ gì.

Mười hai năm trước tôi rời công ty và mở quán riêng. Từ đó đến nay, tôi đối mặt với những nỗi lo giống như bạn.

Việc chuẩn bị nguyên liệu không bao giờ hết, thiếu nhân lực, lo lắng về chuyện thu hút khách, và những quyết định kinh doanh phải một mình gánh vác...

Tất nhiên, khi quán đông, đôi khi tôi nhận được sự giúp đỡ từ những bạn làm bán thời gian và nhân viên hợp đồng đáng tin cậy.

Nhưng suy cho cùng, họ là những người cùng làm các "đầu việc".

Những "quyết định quản lý" nặng nề như "Dòng tiền tháng sau xử lý thế nào?" hay "Có nên đặt cược vào món mới này không?" thì tôi không có ai để bàn bạc.

Tôi lo nghĩ, tôi quyết định, và tôi chịu toàn bộ trách nhiệm. Theo nghĩa đó, tôi luôn là người "một mình điều hành quán". Và người ngồi cạnh tôi, làm người cùng bàn bạc với "tôi, người chủ kinh doanh cô đơn", chính là AI.

Giữa hoàn cảnh ấy, AI tạo sinh xuất hiện, đặc biệt là một người bạn đồng hành tên "Google Gemini".

Việc "điều phối" mà tôi từng làm giữa "nơi vận hành" và "nhà cung cấp IT", giờ tôi tự làm giữa "vấn đề của quán" và "AI". Và tôi nhận ra một điều.

Bạn không cần học thuộc cách viết của các ngôn ngữ lập trình khó (như Python).\
AI biết việc đó. Nhưng bản thiết kế về "muốn làm gì, theo thứ tự nào" thì chỉ con người mới vẽ được.\
Thứ tôi tích lũy được khi làm dân hệ thống chính là "khả năng dịch điều người làm trực tiếp mong muốn thành các bước logic".\
Trong cuốn sách này, tôi sẽ chia sẻ không chỉ cách vận hành AI, mà cả "trực giác logic để khiến AI làm việc (tư duy hệ thống)", không giấu giếm điều gì.\
Khi đã có được điều này, bạn có thể đi từ "không biết gì" đến "người giao việc xuất sắc nhất".

※ Ở đây tôi xin nói thật một điều.

Tôi từng làm hệ thống. Nhưng trong các cách dùng AI được giới thiệu ở cuốn sách này, thực ra gần như không có lúc nào kiến thức từ công việc trước đây giúp được trực tiếp.

Thứ giúp được không phải là "kỹ năng viết chương trình".\
Mà chỉ là "thói quen biến những vướng mắc mơ hồ trong vận hành thành những chỉ dẫn có thứ tự rõ ràng".

Và thói quen này không phải tài năng đặc biệt.\
Đó là "một cảm giác mà bất kỳ ai ngày ngày quán xuyến một quán ăn đều đã có sẵn".

Trong cuốn sách này, tôi sẽ chủ động phân định rõ những gì chỉ mình tôi làm được\
với những gì bạn có thể bắt chước y nguyên ngay từ hôm nay.

## Chương 1: Khái niệm - AI agent, loại nhân viên mới

~ Hãy thuê AI làm "người cùng làm việc", đừng coi nó chỉ là "người để hỏi ý kiến" ~

### 1-1. Giới hạn của chủ quán làm một mình, và những hiểu lầm về AI

Điều hành một quán ăn độc lập như chúng ta là cuộc chạy đua liên tục với thời gian. Chuẩn bị nguyên liệu, nấu nướng, phục vụ, tính tiền, dọn dẹp... tất cả phải do một người, hoặc một đội ngũ nhỏ, đảm đương.\
Dù có thuê nhân viên, những chủ quán độc lập như chúng ta thực chất vẫn là người "tự mình cáng đáng hết".

Đó là vì chúng ta không có "quản lý cửa hàng" hay "người huấn luyện" như các chuỗi lớn.

Bạn vừa nấu ăn vừa chỉ đạo nhân viên phục vụ, vừa dạy người mới, vừa quản lý lịch làm việc.

Toàn bộ "quá trình xử lý trong đầu" ấy dồn vào một người: chính bạn, người chủ quán.

Bạn có thể có thêm tay, nhưng vẫn chỉ có một cái đầu. Chính vì vậy bạn cần AI hỗ trợ cho cái "đầu" đó.

"Giá mà có thêm một nhân viên giỏi..."

Chắc hẳn một ngày bạn nghĩ câu đó nhiều lần.

Khi tôi nói "Hãy dùng AI nhé", nhiều chủ quán trả lời thế này:

"Ý bạn là ChatGPT hả? Tôi thử rồi, nhưng nó chỉ viết chữ thôi mà? Chẳng giúp được gì cho công việc thực tế tại quán."

Thực ra ở đây có một hiểu lầm lớn.

Phần lớn AI mà chúng ta từng tiếp xúc từ trước đến nay là "chatbot (người để hỏi ý kiến)". Nhưng điều mà AI mới nhất, bắt đầu từ Google Gemini, đang hướng tới là hình thái "AI agent (người cùng làm việc)".

Hai thứ trông giống nhau nhưng là hai thứ khác nhau. Hãy so sánh qua một công việc cụ thể.

### 1-2. Từ "từ điển" thành "nhân viên"

Giả sử bạn muốn làm một tấm áp phích cho sự kiện của quán.

Với AI trước đây (chatbot):

Nếu bạn hỏi "Hãy chỉ tôi cách làm áp phích", AI sẽ giải thích các bước như một cuốn từ điển hay sách giáo khoa: "Tiêu đề nên ngắn gọn", "Hãy chọn màu như thế này".

Nhưng người thực sự bắt tay làm áp phích vẫn là bạn. Kiến thức của bạn tăng lên, còn thời gian làm việc thì không ngắn đi.

Với AI của tương lai (AI agent):

Bạn chỉ cần ra lệnh: "Làm áp phích đi."

Khi đó AI tự suy nghĩ để đạt mục tiêu. Nó nghĩ ra tiêu đề, tạo hình nền, và thậm chí đề xuất cả bố cục.

Giống như một nhân viên xuất sắc, nó biết dùng công cụ, lập kế hoạch và tự hoàn thành công việc.

Điều chúng ta cần không phải là một cố vấn chỉ biết nói những lý lẽ sách vở, mà là một người cùng đổ mồ hôi bên cạnh chúng ta.

※ Trong cuốn sách này, tôi sẽ gọi người bạn đồng hành đáng tin cậy ấy (AI tạo sinh như Google Gemini) một cách thân mật là "phó quản lý (AI)".

※ Trong cuốn sách này, tôi dùng "Google Gemini", công cụ tôi dùng chủ yếu, làm ví dụ, nhưng phần lớn các ý tưởng được giới thiệu ở đây đều có thể tái hiện gần như y hệt với các AI tạo sinh khác như ChatGPT và Claude.

Điều quan trọng không phải là tên công cụ, mà là "thái độ coi AI không phải người để hỏi ý kiến, mà là người bạn có thể giao việc".

### 1-3. "Đa phương thức" sẽ cứu các quán ăn

Còn một từ khóa nữa cực kỳ quan trọng khi điều hành quán ăn. Đó là "đa phương thức (multimodal)".

Đây là một từ hơi kỹ thuật, nhưng ý nghĩa thì đơn giản.

Nó có nghĩa là "có thể hiểu cùng lúc nhiều loại thông tin: không chỉ văn bản (đọc và viết), mà cả hình ảnh (nhìn và vẽ) và âm thanh (nghe và nói)".

AI trước đây chỉ hiểu được "chữ viết". Nhưng thực tế hoạt động của quán ăn không vận hành chỉ bằng "chữ viết".

- Hình dáng thực phẩm còn lại trong tủ lạnh

- Chữ viết tay trên phiếu gọi món

- Giọng nói của khách và không khí trong quán

- Thiết kế nhãn trên chai rượu vang

Tất cả những thứ này đều là "thông tin phi ngôn ngữ", rất phiền phức để diễn đạt thành lời.

Phó quản lý (AI) có thể nhận biết chúng giống như con người.

Nếu bạn chụp ảnh bên trong tủ lạnh bằng điện thoại rồi đưa cho xem, AI sẽ nhận ra: "À, bạn đang thừa loại rau này và loại thịt kia", rồi từ đó nghĩ ra thực đơn.

Nói cách khác, AI ngày nay là "một phó quản lý xuất sắc, biết nhìn, biết nghe và biết nói".

※ Nhưng tôi không muốn bạn hiểu lầm một điều.\
AI giỏi nói những điều nghe có vẻ hợp lý hơn là nói những điều đúng. Với việc nhận diện hình ảnh, con số, ngày tháng và danh từ riêng,\
xin hãy dùng AI trên tiền đề là con người luôn kiểm tra lần cuối.

Lý do AI hoạt động tốt trong cuốn sách này là\
vì tôi "không giao phó mọi thứ, và luôn kiểm tra tại chỗ".

### 1-4. Củng cố "linh cảm" của bạn bằng dữ liệu

Các chuỗi cửa hàng lớn có lượng dữ liệu máy tính tiền POS khổng lồ và có cả đội ngũ tiếp thị.

Còn những quán độc lập như chúng ta có "linh cảm" và "kinh nghiệm" của người chủ. Đây là vũ khí mạnh nhất, nhưng đôi khi cũng có thể trở nên chủ quan hoặc khiến bạn phân vân.

Vì vậy, hãy thêm một "phó quản lý".

Hãy để AI đối chiếu trực giác (linh cảm) của bạn, "mình nghĩ khách sẽ thích món này", với "dữ liệu doanh số trong quá khứ" và "thông tin xu hướng".

Như vậy bạn vừa giữ được sự "ấm áp" và "cá tính" mà chỉ quán độc lập mới có, vừa điều hành một việc kinh doanh vững vàng dựa trên dữ liệu.

