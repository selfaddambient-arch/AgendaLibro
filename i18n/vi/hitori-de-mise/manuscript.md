## Lời mở đầu

Cuốn sách này là bản ghi chép tính đến tháng 1 năm 2026. Từ đó đến nay, một số cách tôi vận hành quán, cũng như tên gọi và thông số của các công cụ AI, đã thay đổi. Phần tiếp theo, tôi đã viết trong cuốn thứ hai, *Làm riêng cho quán bar của mình*.

### Vì sao một người từng làm hệ thống lại trò chuyện với AI trong một quán ăn dưới tầng hầm

Cảm ơn bạn đã cầm cuốn sách này lên.

*Một người điều hành cả quán, và AI xuất hiện ngay bên cạnh tôi.*

Thấy tiêu đề ấy, có thể có bạn nghĩ: "Đúng là mình rồi." Cũng có bạn thắc mắc: "AI xuất hiện bên cạnh nghĩa là sao?"

Đây không phải sách kỹ thuật về lập trình khó nhằn. Đây là cuốn sách dành cho những người như bạn, những chủ quán ngày nào cũng đứng trong bếp, lo chuẩn bị nguyên liệu và lúc nào cũng bận rộn với khách.

Trước hết xin giới thiệu đôi chút về tôi.

Hiện nay tôi điều hành một quán ăn nhỏ ở tầng hầm của một tòa nhà tại Higashi-Nakano *(một khu dân cư ở phía tây Tokyo, ngay phía tây Shinjuku)*, Tokyo.

Quán mang hai diện mạo khác nhau. Ban ngày, đó là quán chuyên cà ri thịt viên kiểu hamburger thơm mùi gia vị. Ban đêm, đó là quán bar ăn uống chỉ nhận khách có người giới thiệu, phục vụ set ăn đổi món theo ngày và đồ uống.

▼ Cà ri hamburger Quatre Epice (Instagram)

https://www.instagram.com/quatre.epice.hamburg.curry/

![Cà ri hamburger Quatre Epice (Instagram)](images/fig-01.png)

▼ Quán bar chỉ nhận khách có người giới thiệu "Tamuro" (Instagram)

https://www.instagram.com/tamuro.higashinakano/

![Quán bar chỉ nhận khách có người giới thiệu "Tamuro" (Instagram)](images/fig-02.png)

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

## Chương 2: Kiến thức nền tảng - "Vibe coding" từ con số không

~ Chương trình không phải thứ bạn "viết". Đó là thứ bạn "nhờ AI dựng nên bằng cách trò chuyện". ~

### 2-1. Chẳng ai đọc "tin nhắn LINE dài dằng dặc". Phép màu của "sơ đồ" chỉ mất 30 giây

Nói đến chuyện "dùng AI để xây dựng một hệ thống", có thể bạn vẫn thấy hơi cao xa.

Vậy nên hãy bắt đầu bằng một "cách dùng AI" quen thuộc hơn, có thể áp dụng ngay từ hôm nay.

Đó là một cuộc cách mạng trong việc "giao việc cho nhân viên".

Nhiều chủ quán như chúng ta dùng LINE *(ứng dụng nhắn tin phổ biến nhất ở Nhật)* để liên lạc với nhân viên.\
Tôi thường điều hành quán với số người hạn chế, và vào giờ phục vụ đông khách thì không có thời gian để thong thả chỉ dẫn cặn kẽ.

Vì thế, việc thông báo chắc chắn phải dựa vào tin nhắn LINE sau giờ đóng cửa.

Nhưng chỉ bằng lời thì cực kỳ khó truyền đạt hình dung "tôi muốn làm thế này", thứ chỉ tồn tại trong đầu mình, cho nhân viên còn ít kinh nghiệm hay người thỉnh thoảng đến phụ giúp.

Đó chính là nguồn gốc của "tin nhắn LINE dài dằng dặc".

Càng cố giải thích kỹ, văn bản càng dài ra, và kết quả là...

"À, xin lỗi, em chưa đọc tới đó."

"Toàn chữ là chữ, em không biết đoạn nào quan trọng."

Những chuyện như vậy có xảy ra ở chỗ làm của bạn không?

Với tôi cũng đã từng.

Một hôm, vì một ứng dụng đang phát triển, tôi thử nhờ một nhân viên chụp "ảnh nguyên liệu".

Điều kiện hơi phức tạp, nên phần chỉ dẫn tôi gõ trên điện thoại đã thành một tin nhắn dài như thế này.

![Tin nhắn LINE dài mà tôi thực sự đã gửi cho nhân viên, kể cả lỗi chính tả](images/fig-03.jpg)

Dù nhìn thấy cái này, nhân viên bếp đang bận rộn cũng sẽ lướt qua với suy nghĩ "tóm lại là chụp ảnh thôi đúng không?" và bỏ sót những yêu cầu về "góc chụp" và "hướng đặt đồ đựng".

Nhưng tôi không có thời gian mở PowerPoint, chèn các hình khối rồi làm một tờ hướng dẫn công việc.

Thế là tôi đưa nguyên văn bản này cho AI (một công cụ AI như Manus hay Gemini) và nhờ:

"Hãy tóm tắt nội dung văn bản này trên một slide, dưới dạng 'phiếu hướng dẫn công việc' để nhân viên nhìn là hiểu ngay."

### 2-2. AI là một "người biên dịch xuất sắc"

Sau vài giây chờ đợi, thứ AI tạo ra là một "slide sơ đồ" dễ hiểu đến bất ngờ.

![Slide "Hướng dẫn thu thập dữ liệu và chụp ảnh" do AI tự động tạo ra](images/fig-04.jpg)

Tôi không thiết kế gì cả. Tôi chỉ nói: "Đây là văn bản, hãy tóm tắt giúp tôi."

Từ đoạn văn lan man của tôi, AI hiểu ngay "điều gì quan trọng" và "nên phân loại thế nào", rồi "dịch" nó thành một bố cục mà con người nắm bắt được bằng trực giác.

### 2-3. Thoát khỏi "nỗi bực mình vì nói mà người khác không hiểu"

Tôi dán hình này vào LINE rồi gửi đi.

Hiệu quả thấy ngay.

Nhân viên không hỏi lại điều gì, và ngay lần đầu đã gửi về dữ liệu ảnh hoàn hảo, chụp "theo chiều dọc" với "3 góc".

Trước đó, tôi từng bực với nhân viên, nghĩ "Sao họ không chịu đọc nhỉ?", và cũng từng lo: "Có lẽ mình giải thích dở thôi."

Nhưng người đáng trách không phải nhân viên, cũng không phải tôi. Đó là "việc truyền đạt chỉ bằng chữ".

Trải nghiệm này đã thay đổi cách tôi nhìn AI.

AI không chỉ là công cụ để "tạo từ đầu" văn bản và hình ảnh mới.

Nó là "công cụ 'chuyển đổi' những 'ý tứ khó truyền đạt đến người nghe' của chúng ta thành một dạng mà đối phương tiếp nhận được".

### 2-4. "Vibe coding", một kiểu đối thoại mới

Khi đã quen trò chuyện với AI, bước tiếp theo cuối cùng cũng là "xây dựng công cụ".

Có thể bạn nghĩ: "Lập trình thì mình bó tay", nhưng đừng lo.

Hiện nay, trong giới kỹ sư, có một thuật ngữ đang được bàn tán sôi nổi là "vibe coding".

Đó là phương pháp mà thay vì con người viết những dòng mã khó nhằn, bạn dựng nên hệ thống bằng cách trò chuyện với AI như thể đang hòa hợp "vibe" (cảm giác và không khí).

Sota Fujii, kỳ thủ cờ shogi giữ danh hiệu Meijin, đã nêu "vibe coding" là thứ mình bắt đầu mê trong năm nay, năm 2025. Nghe nói ngay cả một người từ làng shogi, vốn tưởng chẳng liên quan gì đến việc xây dựng hệ thống, cũng nói với AI điều mình muốn bằng tiếng Nhật và tạo ra những công cụ tiện dụng.

Nhờ trò chuyện với AI, chúng ta cũng có thể xây dựng hệ thống mà không cần kiến thức chuyên môn.

Thứ bạn dùng chỉ là "tiếng Nhật". Khi bạn nói: "Tôi muốn nó chạy thế này" hay "Chỗ này khó dùng quá", phó quản lý (AI) sẽ viết mã ở phía sau.

Nói cách khác, bạn không cần trở thành "lập trình viên".

Bạn chỉ cần trở thành "người chỉ huy tại hiện trường" biết giao việc cho một "kỹ sư xuất sắc (AI)".

### 2-5. "Than phiền" ở quán của bạn chính là prompt mạnh nhất

Chỉ dẫn cho AI (prompt) không cần dùng những lời hoa mỹ.

Prompt mạnh nhất mà tôi khám phá ra là "những điều 'bất tiện' và 'bực mình' ở quán của bạn, hay nói cách khác là những lời than phiền của bạn".

- "Ngày nào cũng phải làm phép tính này, phiền quá."

- "Tôi không muốn chỉnh kích thước ảnh bằng tay."

Với AI, đó đều là những "yêu cầu phát triển" thực thụ.

Một cảm giác như "ghét cái này quá" gợi ra giải pháp cụ thể dễ hơn một mục tiêu kiểu "tôi muốn làm điều này".

### 2-6. Lỗi không phải là "thất bại". Đó là "khởi đầu của một cuộc đối thoại"

Khi bắt đầu làm gì đó cùng AI, chắc chắn bạn sẽ gặp "lỗi".

Nhưng trong vibe coding, lỗi không phải là thất bại.

Đó là "tín hiệu cho thấy màn đối thoại qua lại hai chiều với AI đã bắt đầu".

Ngay cả giữa con người với nhau, hiếm khi ý mình được hiểu trọn vẹn ngay lần đầu.

Khi AI báo lỗi, bạn cứ nhẹ nhàng gạt đi với "À, mình nói chưa tới", rồi nói lại: "Không, điều tôi muốn là thế này."

Hãy giữ nhịp trao đổi qua lại mà không bỏ cuộc. Chỉ cần làm được vậy, ngay cả bạn, dù không có chút kiến thức nào, chắc chắn vẫn xây được "một hệ thống chỉ của riêng bạn".

### 2-7. Tăng hiệu suất vượt bậc với "nút bấm vật lý" - dùng bàn phím phụ

Trong vibe coding, điều quan trọng nhất là "chăm chút khâu nhập liệu".

Cuộc trò chuyện với AI càng nhanh thì dòng suy nghĩ càng ít bị ngắt quãng, và quá trình phát triển càng tiến nhanh. Ngược lại, nếu bạn vấp ở khâu nhập liệu, ngay cả ý tưởng hay cũng có thể tan biến.

Trước đó tôi đã nói với bạn: "Khi xuất hiện lỗi, cách đúng là chụp màn hình rồi dán vào."

Nhưng việc bấm [Windows] + [Shift] + [S] (Mac: [Cmd] + [Shift] + [4]) hàng chục lần mỗi ngày, chọn vùng bằng chuột, quay lại màn hình Gemini rồi bấm [Ctrl] + [V] (Mac: [Cmd] + [V])...

Thật lòng mà nói, nó làm mỏi ngón tay, đúng không?

Vì vậy, thứ tôi giới thiệu là "bàn phím phụ 6 nút".

Đó là một chiếc bàn phím nhỏ sản xuất tại Trung Quốc, giá từ vài trăm đến khoảng một nghìn yên, hiện ra khi bạn tìm "programmable keyboard" trên Amazon hay các trang tương tự.

![Ảnh chiếc bàn phím phụ 6 nút tôi đang dùng](images/fig-05.jpg)

Tôi đã gán các phím tắt sau cho sáu nút này.

1.  Mở chụp màn hình

2.  Chọn tất cả (Ctrl + A; Mac: Cmd + A)

3.  Sao chép (Ctrl + C; Mac: Cmd + C)

4.  Dán (Ctrl + V; Mac: Cmd + V)

5.  Enter (gửi)

6.  (Dự phòng)

Chỉ có vậy. Nhưng hiệu quả thì rất đáng kinh ngạc.

Một lỗi xuất hiện.

↓

Bằng tay trái, tôi bấm "Nút 1 (chụp màn hình)".

↓

Tôi chọn vùng cần chụp, rồi bấm "Nút 4 (dán)" trên màn hình Gemini.

↓

Bấm "Nút 5 (gửi)".

Tất cả chỉ mất 2 giây.

Bạn không cần nhớ phím tắt hay di chuyển ngón tay phức tạp.

Bạn có thể ném thông tin cho AI như đang điều khiển tay cầm chơi game.

Như bạn sẽ thấy ở các chương sau, khi sửa mã nguồn do AI xuất ra, chỉ cần chọn tất cả (Ctrl + A), sao chép (Ctrl + C) và dán (Ctrl + V) là bạn có thể chạy lại ngay, rất tiện.

Trước khi học kiến thức lập trình nâng cao, hãy thử sắm trước món thiết bị nhỏ này.

Loại bỏ về mặt vật lý "sự phiền toái khi nhập liệu". Đó là con đường tắt chắc chắn nhất để tăng tốc cuộc trò chuyện với người bạn đồng hành AI của bạn.

## Chương 3: Thực hành 1 - Tự động hóa công việc sáng tạo và thu hút khách

~ "Dán ảnh chụp màn hình rồi giao hết cho AI" hóa ra là phương pháp phát triển mạnh nhất ~

### 3-1. Thử và sai để xóa đi "chất AI" (sticker LINE)

Khi đã quen với việc trò chuyện bằng văn bản (vibe coding), cuối cùng tôi quyết định thử sức với "tạo hình ảnh".

Để luyện tay, tôi chọn làm "sticker LINE", thứ cũng có thể giúp quán gắn kết và thu hút thêm khách quen.

Nhưng những "bức tranh bóng mịn như đồ họa máy tính" vốn đặc trưng của ảnh do AI tạo ra lại không hợp với không khí của quán tôi.

Điều tôi nhắm tới là "phong cách phẳng kiểu retro những năm 1980, mang nét vẽ tay, giữ được chất liệu của bút sáp màu và cọ".

Từ đó bắt đầu một cuộc "trò chuyện" dài giữa tôi và phó quản lý (AI).

Lúc đầu, tôi bắt đầu với các nhân vật là "hai cậu bé và một chú chó Shiba Inu".

"Cho tôi 25 mẫu hội thoại thường ngày."

"Làm độ dày nét vẽ ngẫu nhiên, như nét cọ."

Từng chút một, như đang đưa yêu cầu chỉnh sửa cho một họa sĩ minh họa là con người, tôi kiên nhẫn dạy nó gu mà tôi thích.

![Các hình minh họa do AI tạo ra cho sticker LINE](images/fig-06.png)

### 3-2. Yêu cầu táo bạo: "Chỉ đổi chú chó thành mèo"

Khi mọi thứ đã có hình có dạng, tôi quyết định đổi hướng lớn: "Nghĩ lại thì, tôi muốn đổi thành các cô gái và một con mèo."

Một họa sĩ minh họa bình thường sẽ nhăn mặt và nói: "Gì cơ, làm lại từ đầu sao?" Nhưng phó quản lý (AI) không phàn nàn lấy một lần.

"Đổi nhân vật thành hai cô gái, một người tóc dài và một người tóc ngắn. Quần áo màu vàng và xanh lá, cùng phong cách vẽ tay như trước."

"Đổi chú chó thành mèo, chuyển lời thoại sang kiểu mèo nói mà bạn đã tạo trước đó, và làm các tư thế cho phù hợp."

"Làm con mèo thành mèo Xiêm, không phải mèo vằn vàng."

Hơn nữa, tôi còn đưa ra một yêu cầu thử thách giới hạn của AI.

"Giữ nguyên bố cục của 'các cậu bé và chú chó Shiba Inu' mà bạn đã làm trước đó, chỉ vẽ lại phần con chó thành một con mèo Xiêm."

Thật bất ngờ, AI đã hiểu được chỉ dẫn phức tạp này. Vị trí và tư thế của các cậu bé vẫn y nguyên, trong khi người và con vật được thay gọn gàng, thành các cô gái và một "chú mèo Xiêm".

![Bảng hình minh họa sticker LINE hoàn chỉnh](images/fig-07.png)

Tuy nhiên, để dùng làm sticker trên LINE, bạn cần tách các hình minh họa ra, tạo ảnh thu nhỏ, nén tất cả vào một tệp ZIP rồi tải lên.

Việc này cũng có thể làm qua trò chuyện với Gemini, nhưng tôi sẽ trình bày cụ thể hơn ở phần 3-6. Ải khó đầu tiên: Tách ảnh đơn giản và "cái bẫy chất lượng ảnh".

### 3-3. Trường hợp 2: "Banner Giáng sinh" được làm qua 22 lượt trò chuyện

Sau sticker LINE, còn một sản phẩm lớn nữa mà tôi đã làm cùng AI. Đó là banner thông báo cho "bữa tối Giáng sinh", sự kiện lớn nhất năm của quán.

Tôi dùng một AI có tên "Nano Banana" (mô hình tạo ảnh được tích hợp trong Gemini của Google).

#### Giai đoạn 1: Chỉnh bố cục và chữ

Lúc đầu, tôi bắt đầu bằng việc đặt các yếu tố cần thiết (ông già Noel, tuần lộc, thông tin chữ) lên một khung vẽ khổ ngang.

Nhìn những bức ảnh vừa ra, tôi đưa chỉ dẫn.

"Hơi trống một chút. Thêm hình minh họa cây thông Noel và rượu sâm panh."

"Thực đơn là danh sách gạch đầu dòng nên khó đọc. Gói gọn lại thành 'tổng cộng sáu món', và làm tiêu đề to hơn, bắt mắt hơn."

![Hình ảnh được tạo ra ở giai đoạn đầu, trông còn hơi trống trải](images/fig-08.png)

#### Giai đoạn 2: Chỉnh độ "rộn ràng"

Khi bố cục đã ổn, tiếp theo là bầu không khí. Nó thiếu "cảm giác tiệc tùng".

Tôi chỉ dẫn: "Làm rộn ràng hơn! Rải thật nhiều ông già Noel và tuần lộc nhỏ, bóng bay và hoa giấy."

Lần này, khung hình trở nên quá rối mắt.

"Xin lỗi, nhiều yếu tố quá. Giảm bớt nhân vật đi rồi làm cho gọn gàng."

Có thể lặp lại việc tinh chỉnh kiểu "thêm vào, bớt đi" như vậy chính là thế mạnh của AI.

#### Giai đoạn 3: Ý tưởng bất ngờ về việc "làm lại hoàn toàn"

Giữa chừng quá trình làm, một nỗi băn khoăn len vào. "Chẳng phải cho xem hình các món ăn, thay vì lấy nhân vật làm chính, thì trông sẽ ngon hơn sao?"

Vì thế tôi mạnh dạn chỉ dẫn: "Như một phương án khác, hãy làm một thiết kế lấy hình minh họa các món ăn thực tế làm yếu tố chính."

![Bản phác thảo minh họa với các món ăn (một số chữ bị lỗi)](images/fig-09.png)

AI lập tức đưa ra những ý tưởng minh họa món ăn trông rất hấp dẫn, nhưng sau khi so sánh, rốt cuộc tôi vẫn chọn thiết kế nhân vật ban đầu. Ngay cả một yêu cầu kiểu "quay lại như cũ nhé" thế này cũng có thể nhờ AI mà không cần ngại ngần.

#### Giai đoạn 4: Tuyến phòng thủ cuối cùng là con mắt "con người"

Sau khi thiết kế cuối cùng được chốt, tôi cũng giao cho AI các biến thể kích thước, cho bài đăng Instagram (dọc) và cho Stories (còn dài hơn nữa).

Rồi ngay lúc sắp hoàn thành, tôi nhận ra một lỗi nghiêm trọng.

"Khoan, thứ trong tuần của ngày tháng bị sai rồi!"

AI giỏi vẽ tranh, nhưng không hiểu các thứ trong tuần trên lịch. Nếu cứ đăng nguyên như vậy thì đúng là thảm họa.

Tôi vội chỉ dẫn: "Sửa ngày thành '24/12 (Thứ Tư) và 25 (Thứ Năm)'!" và hoàn thành bản cuối.

![Banner cuối cùng sau khi chỉnh sửa](images/fig-10.png)

Tổng cộng 22 lượt chỉnh sửa và trò chuyện.

AI không phải cây đũa thần, nhưng nếu kiên nhẫn trò chuyện với nó, sẽ không có đối tác thiết kế nào đáng tin cậy hơn.

### 3-4. Trường hợp 3: Thông báo mở cửa dịp Tết Dương lịch tiến hóa theo tình hình

Không khí rộn ràng của Giáng sinh còn chưa kịp nguội thì sự kiện tiếp theo đã đến: kinh doanh cuối năm và đầu năm mới.

Với một quán ăn hay quán bar, cập nhật thông tin vào thời điểm này là cuộc chạy đua với thời gian. "Cuối năm quán mở đến khi nào?" "Sang năm mới khi nào quán mở lại?" Khách luôn tìm kiếm thông tin.

Nhưng thông tin thay đổi từng phút.

"Khi dịp cuối năm kết thúc, tôi muốn viết lại để chỉ còn hiện thông báo năm mới."

"Tôi đã đăng lên X (ngang), nhưng tôi cũng muốn đăng trên Instagram (dọc)."

Nếu nhờ một nhà thiết kế bên ngoài làm việc này, riêng phí chỉnh sửa thôi cũng đã là cơn ác mộng, và trên hết là không kịp thời gian.

Vì vậy, một lần nữa tôi bắt tay với AI tạo ảnh (Nano Banana) và bắt đầu làm các banner để đồng hành cùng tôi suốt mùa cuối năm và đầu năm mới.

#### Bước 1: Phong cách là "tranh bút sáp thập niên 80"

Trước tiên, tôi dựng nên diện mạo và cảm giác chung.

Thứ hợp với quán bar của tôi không phải là đồ họa máy tính bóng bẩy.

"Phong cách ấm áp như một bức tranh bút sáp vẽ tay thời thập niên 80, thấy rõ nét cọ. Giữ nền trắng trơn."

Với chỉ dẫn này làm cốt lõi, và nghĩ tới thông báo trên X (trước đây là Twitter), tôi bắt đầu làm trên khung tranh ngang.

#### Bước 2: Con rắn ra đi và con ngựa đến. Cụng ly trao tay nhau cây gậy tiếp sức

Lúc đầu tôi định chỉ vẽ một con giáp, nhưng dù sao đây cũng là thời khắc chuyển giao năm.

Tôi nảy ra một ý: "Tôi muốn cả con giáp của năm cũ (con giáp năm nay) lẫn con giáp của năm mới (năm sau) cùng xuất hiện."

Thế là tôi đưa cho AI chỉ dẫn này:

"Đặt một nhóm rắn (năm Tỵ) ở bên trái màn hình và một nhóm ngựa (năm Ngọ) ở bên phải. Cho mỗi con cầm một cốc bia và vui vẻ cụng ly, như đang trao nhau cây gậy tiếp sức vào cuối năm."

Hình ảnh AI tạo ra đúng y như những gì tôi hình dung.

Những chú rắn dễ thương ở bên trái, những chú ngựa trông đáng tin cậy ở bên phải, vượt qua ranh giới giống loài để cùng nhau nâng ly.

Từ "cuối năm (Tỵ)" sang "năm mới (Ngọ)".

Chỉ trong một bức tranh, dòng chảy thời gian và không khí lễ hội được cô đọng thật đẹp.

![Hình do AI tạo ra: con rắn bên trái và con ngựa bên phải nâng ly, thể hiện năm cũ nhường chỗ cho năm mới](images/fig-11.png)

#### Bước 3: "Chỉ đạo diễn xuất" và "thử trang phục" cho các con vật

Khi bố cục đã định, việc tiếp theo là dàn dựng chi tiết hơn. Ở đây cũng vậy, AI vẫn kiên nhẫn đáp ứng những đòi hỏi tỉ mỉ của tôi.

Trong những bức ảnh đầu tiên, các con vật chỉ đứng thành hàng, hoặc cầm cốc theo những tư thế không tự nhiên.

"Làm cho trông vui hơn nữa! Như những vị khách quen đang có khoảng thời gian tuyệt vời bên nhau."

"Tôi cũng muốn có cảm giác mùa. Cho chúng đeo khăn quàng và nơ, tạo dáng vẻ mùa đông."

Chỉ với một câu đó, các con vật trên màn hình quấn những chiếc khăn quàng đỏ và xanh lá trông thật ấm áp, và lập tức biến thành những ngôi sao của "bữa tiệc mùa đông".

"Đúng rồi, giờ đã có cảm giác ấm áp của việc uống rượu ban ngày trong ngày lạnh."

Nhìn kỹ thì một số động tác tay và cách cầm cốc vẫn chưa tự nhiên. Nhưng càng cầu kỳ thì càng mất thời gian. Cân đối giữa thời gian và mức độ truyền tải thông điệp, tôi chấp nhận một kết quả khá tốt.

#### Bước 4: Thời gian trôi, thông tin thay đổi

Từ đây trở đi mới là lúc AI thật sự cho thấy giá trị.

Banner gốc hiển thị cả lịch tháng 12 và tháng 1 với tiêu đề "Lịch kinh doanh cuối năm và đầu năm mới".

Nhưng khi ngày 31 tháng 12 đã qua, thông tin cuối năm không còn cần thiết nữa.

Tôi mở dự án đang làm dở và yêu cầu thay đổi lớn phần chữ.

1.  Đổi tiêu đề: từ "Lịch mở cửa cuối năm và đầu năm mới" thành "Đầu năm quán mở cửa phục vụ uống ban ngày."

2.  Tinh gọn thông tin: xóa lịch tháng 12 đã qua và thu gọn chỉ còn "lịch năm mới (2/1-4/1)."

3.  Sửa nhân vật con giáp: đổi những chú rắn của năm cũ thành ngựa.

4.  Thêm điểm thu hút: thêm ưu đãi hấp dẫn "highball và gà rán ăn uống thỏa thích" như một sức hút mới với khách.

![Bước 4: Thông tin thay đổi theo thời gian](images/fig-12.png)

Không cần tạo lại hình từ đầu, tôi vẫn làm mới được thông tin như viết lại chữ trên tấm bảng đen. Đó là sức mạnh của thiết kế bằng AI.

#### Bước 5: Từ X sang Instagram. Định dạng biến hóa linh hoạt

Và bây giờ là bước hoàn thiện cuối cùng.

"Tôi đã thông báo trên X rồi. Tiếp theo tôi muốn đăng trên Instagram Stories."

Nhưng Stories dùng kích thước "dọc", lấp đầy cả màn hình điện thoại. Nếu đưa nguyên một bức ảnh ngang vào, sẽ có những dải trống phía trên và phía dưới, trông rất xấu.

Với một bức minh họa thông thường, đây là kiểu thay đổi đồng nghĩa với việc phải vẽ lại.

Nhưng tôi chỉ việc nói với AI:

"Giữ nguyên thiết kế này, nhưng sắp xếp lại thành bố cục dọc cho Instagram Stories."

AI sắp xếp lại các con vật vốn trải ra theo chiều ngang thành bố trí theo chiều dọc, chỉnh cân đối phần chữ, và lập tức tạo ra một thiết kế vừa vặn cho điện thoại thông minh.

![Hình dọc hoàn chỉnh cho Instagram Stories](images/fig-13.png)

### 3-5. Trường hợp 4: Làm logo cho quán - Cuộc trò chuyện biến "ý nghĩa" thành "hình hài"

Ngoài những "bức tranh" như banner và sticker, tôi còn cùng AI đảm nhận một thử thách trừu tượng hơn: thiết kế một logo mới.

Logo này dự định được đưa vào banner và các ấn phẩm tương tự, để mọi người nhận ra Tamuro ngay từ cái nhìn đầu tiên.

Đối tượng ở đây là Tamuro, quán bar chỉ nhận khách có người giới thiệu mà tôi điều hành vào ban đêm. Cái tên này gửi gắm một tâm nguyện tha thiết: "trở thành nơi đủ mọi kiểu người được thoải mái tụ họp và vui vẻ (tamuro-suru, tức là tụ tập, quây quần) ở khu Higashi-Nakano."

Làm thế nào để cô đọng "câu chuyện" vô hình ấy thành một biểu tượng logo nhỏ? Một cuộc đối thoại kiên nhẫn với AI đã bắt đầu.

#### Bước 1: Chọn kiểu chữ và hướng thiết kế

Lúc đầu tôi tung ra cho AI đủ loại ý tưởng, chẳng hạn "vẻ trầm tĩnh với chữ Hán 屯" hay "kiểu sôi động bằng katakana", rồi nhờ nó phác ra vài bản nháp.

Nhưng chẳng bản nào ưng ý. Với tính chất của quán, tôi muốn thứ gì hiện đại hơn, có cảm giác trung tính, đón nhận sự đa dạng.

Thế là tôi đổi hướng.

"Hãy lấy chữ cái Latin dễ dùng 'TAMURO' làm gốc. Phong cách là 'thiết kế phẳng' (flat design), không trang trí rườm rà. Và màu sắc phải trông mạnh mẽ ngay cả khi chỉ dùng một màu."

AI lập tức đề xuất chữ "TAMURO" không chân, đơn giản và đậm nét.

![Logo chữ không chân](images/fig-14.png)

#### Bước 2: Thổi "ý nghĩa" vào hình dạng

Từ đây mới là phép thử thật sự. Những con chữ trơn thì chẳng có nghĩa gì. Mà chỉ có mỗi chữ "M" ở giữa thì cũng không truyền đạt được bao nhiêu.

"Tôi muốn thể hiện nguồn gốc cái tên, tức là 'mọi người tụ họp'. Bạn có thể gom toàn bộ vào một 'vòng tròn' thân thiện, đồng thời tạo hình từng chữ cái sao cho trông như một người đang vui vẻ chuyển động không?"

Đây là một yêu cầu rất trừu tượng. Nhưng trí tưởng tượng của phó quản lý (AI) đã vượt xa mong đợi của tôi.

Điều AI nghĩ ra là một thiết kế trong đó khung của các chữ "T", "A", "M" và những chữ còn lại biến thành bóng dáng những người đang nhảy múa, tay chân dang rộng.

![Logo cách điệu chữ cái thành dáng người](images/fig-15.png)

#### Bước 3: Giằng co giữa thiết kế và khả năng đọc

"Thú vị đấy! Nhưng thế này thì không đọc được 'TAMURO' mất..."

Nếu dồn quá nhiều vào thiết kế thì nó không còn nhận ra được là chữ, còn nếu dồn vào chữ thì lại mất đi nét duyên. Tôi đã vấp phải thế tiến thoái lưỡng nan này.

Từ đó trở đi là chuỗi những lần tinh chỉnh lặp đi lặp lại.

"Chữ 'A' trông như một con người, thế là tốt, nhưng hãy nhấn mạnh thêm cấu trúc chữ 'A' của nó. Vẽ thanh ngang cho thật chắc."

"Cân bằng tổng thể thì ổn, nhưng những người đứng sát nhau quá nên trông chật chội. Hãy chừa thêm một chút khoảng trống tươi vui."

"Kết hợp những người đang nhảy múa lúc nãy với các chữ TAMURO, rồi làm thành hình tròn nhé!"

![Biểu tượng logo "TAMURO" hình tròn, hoàn thành sau nhiều lần thử và sửa](images/fig-16.png)

Dù được tạo nên từ những bóng người sống động, chỉ cần nhìn phần dưới là bạn đọc rõ ràng được "TAMURO".

Nhờ trao đi đổi lại ý tưởng với AI hết lần này đến lần khác, tôi đã có được một logo ưng ý, kết hợp khả năng đọc, chất lượng thiết kế và trên hết là "tâm huyết" tôi gửi gắm vào quán.

Hiện nay nó được dùng làm biểu tượng cho các tài khoản X (trước đây là Twitter) và Instagram của quán.

### 3-6. Cửa ải đầu tiên: Cắt đơn giản và "cái bẫy chất lượng ảnh"

Thử thách sáng tạo là làm ra logo đã xong.

Nhưng công việc vẫn chưa hết.

Quay lại với bộ sticker LINE. Thứ tôi đang có trong tay là một "tờ" với 25 hình minh họa được vẽ trên cùng một trang.

Để đăng ký chúng làm sticker LINE, tôi phải cắt từng hình ra, làm nền trong suốt và đổi kích thước. Đó là một việc tẻ nhạt mà tôi cứ trì hoãn mãi.

"Không đời nào tôi cắt tay từng cái được..."

Tôi hỏi Gemini để tìm cách giải quyết. Gemini nói nhẹ tênh như không:

"Hãy tự động hóa bằng một ngôn ngữ lập trình tên là Python."

Thật lòng mà nói, tôi suýt bỏ cuộc ngay tại đó.

"Python ư? Tôi có nghe tên, nhưng cài loại phần mềm đó vào máy tính thì đáng sợ lắm. Nghe nói cài đặt cũng khó. Xin đừng kỳ vọng nhiều như vậy ở một người chỉ điều hành quán bar..."

Nhưng đây là một trong những điểm sáng của cuốn sách. Như thể đoán được tôi đang nghĩ gì, Gemini đưa ra một gợi ý bất ngờ.

Gemini:

"Bạn không cần thiết lập môi trường nào cả. Hãy dùng một công cụ miễn phí của Google tên là 'Google Colab'. Nó chạy ngay trong trình duyệt, nên bạn chỉ cần sao chép rồi dán đoạn mã tôi viết vào đó là chạy được ngay."

"Hả? Lại có thứ như vậy sao?"

Tôi không tin vào tai mình. Tôi chưa từng nghĩ lại có một môi trường có thể lập trình và chạy mã ngay trên trình duyệt, không cần cài gì vào máy tính của mình.

Không phải "sau khi học Python", mà là "được AI dạy cho biết ngay cả sự tồn tại của công cụ (Colab)".

Khoảnh khắc ấy, quan niệm cố hữu của tôi rằng "lập trình nghĩa là phải chuẩn bị rất nhiều thứ" đã sụp đổ.

### 3-7. Đừng "đọc" màn hình lỗi, hãy "chụp rồi gửi"

Làm theo hướng dẫn, tôi mở Google Colab, dán đoạn mã vào và bấm nút chạy (Run).

Nhưng thực tế đâu có dễ dàng như vậy. Thứ hiện lên trên màn hình là hàng loạt dòng chữ đỏ rực... một thông báo lỗi.

"Error: Image file not found..."

Tôi của ngày xưa chỉ cần nhìn thấy thông báo lỗi này là đã dị ứng và lặng lẽ đóng trình duyệt.

Nhưng giờ tôi đã có một đồng minh: AI "đa phương thức", một AI có đôi mắt.

Tôi thậm chí không thử đọc thông báo lỗi.

Tôi chỉ chụp ảnh màn hình rồi dán thẳng vào khung chat của Gemini.

Và thêm đúng một dòng: "Có lỗi gì đó hiện ra."

![Dán nguyên màn hình lỗi của Google Colab vào Gemini](images/fig-17.png)

Gemini phân tích hình ảnh ngay và gửi lại câu trả lời.

Gemini:

"À, tên tệp của hình ảnh đang được tải bị sai. Tôi đã sửa mã để dùng '.jpg'. Hãy chạy lại bằng phiên bản này."

"...Chà, vui thật đấy!"

Cuộc trao đổi này giống một trò "tìm điểm khác biệt" hay một trò ném bắt bóng hơn là lập trình.

- Tôi: (dán ảnh chụp màn hình) "Nó lại dừng rồi."

- Gemini: "Kích thước ảnh không khớp. Tôi sẽ thêm một hàm tự động điều chỉnh."

- Tôi: (dán ảnh chụp màn hình) "Lần này ảnh có vẻ bị vỡ hạt."

- Gemini: "Tôi quên thêm bước xử lý tên là 'LANCZOS' để giữ nguyên chất lượng ảnh. Tôi sẽ sửa."

Tôi không hiểu nổi một dòng mã nào. Mỗi khi có lỗi, tôi chỉ chụp màn hình rồi ném cho AI kèm câu "Xem này!"

Việc "giao phần phân tích lỗi cho AI" này là bí quyết lớn nhất giúp tôi, một người không có chút kiến thức nào, xây dựng được một hệ thống, và đồng thời cũng là trải nghiệm hào hứng nhất trong tất cả.

### 3-8. Bức tường lớn nhất: "Lệch nét vẽ tay" và "tràn ô"

Cứ duy trì "cuộc trò chuyện mang tên lỗi" như vậy, hệ thống ngày càng được trau chuốt.

Và cuối cùng tôi bước vào thử thách lớn nhất: "Giai đoạn 2: Tự động cắt bố cục vẽ tay."

Tôi đã tham lam.

"Hãy làm một tờ 5×5 gồm 25 sticker. Và vì tôi muốn có cảm giác thủ công hơn, nên tôi muốn đặt chúng tự do, không bị ràng buộc bởi các đường kẻ ô."

Với đoạn mã chỉ chia đều tờ giấy, tay hay chữ của nhân vật sẽ tràn sang ô bên cạnh và bị cắt cụt một cách thảm hại.

Tôi cũng thử cách "cắt lấy mọi thứ trừ nền trắng", nhưng phần lề lúc dày lúc mỏng và nó thất bại.

Tôi sắp bỏ cuộc. Rồi, dựa vào trực giác từ thời làm hệ thống, tôi nói với Gemini:

"Tôi muốn bạn bỏ ý định cắt ảnh bằng kéo. Thay vào đó, hãy xem 'điểm giữa' của mỗi bức tranh nằm trong ô nào. Nếu điểm giữa nằm trong ô đó thì dù có tràn ra một chút, cũng hãy coi cả bức tranh là 'thuộc về ô đó' và bỏ vào cái xô của ô đó."

Đây là giải pháp mà tôi đặt tên là "phương pháp xô lưới".

Vì sao tôi lại nghĩ ra việc "bỏ vào xô theo điểm giữa" thay vì "cắt bằng kéo"?

Cách nghĩ của người ngoại đạo (thủ công, analog): Bạn hình dung việc "dùng kéo cắt một bức tranh". Làm vậy thì bạn cắt đúng theo đường kẻ, và tay chân nhân vật sẽ bị cắt cụt mất.

Cách nghĩ của dân hệ thống (kỹ thuật số): Máy tính không có cảm giác vật lý về việc "cắt". Thay vào đó, nó có "tọa độ (vị trí)". Tôi đã nhìn như thế này: "Dù có tràn ra một chút, miễn là 'rốn (điểm giữa)' của bức tranh nằm trong ô, thì ta cứ coi cả bức tranh là 'thuộc về ô này'."

![Tư duy analog "cắt theo đường kẻ" và tư duy kỹ thuật số "chọn theo điểm"](images/fig-18.png)

Đây chính là ý nghĩa của việc "biến thao tác thủ công (analog) mơ hồ thành quy tắc kỹ thuật số rõ ràng". Khi đưa chỉ dẫn cho AI, nghĩ ra một quy tắc như thế này, quy tắc mà kết quả ra giống nhau "dù ai nhìn (hay tính)", sẽ phát huy hiệu quả.

Gemini đã biến yêu cầu trừu tượng này thành mã một cách tuyệt đẹp. Kết quả hoàn hảo.

Dòng chữ "Cảm ơn bạn!" và những cái đuôi tràn sang ô bên cạnh đều được nhận diện gọn gàng và gom lại thành từng sticker riêng.

Nó còn đáp ứng cả yêu cầu có phần tùy hứng của tôi: "Cái cuối cùng (thứ 25) không cần, hãy bỏ qua." Cuối cùng, tôi đã có một công cụ mà "chỉ cần thả ảnh vào rồi bấm một nút là ra trọn bộ ảnh cho ứng dụng LINE".

Tất cả những gì tôi làm chỉ là truyền đạt "vấn đề thực tế khi làm (các bức tranh bị cắt cụt)" và đề xuất một "giải pháp logic (quyết định theo điểm giữa)". Toàn bộ phần mã khó là do AI viết.

Đây chính là cốt lõi của "vibe coding", tức xây dựng hệ thống bắt đầu từ con số không về kiến thức.

#### Tóm tắt Chương 3

1.  Vẽ bằng AI không phải "một lần là xong". Bạn có thể làm lại bao nhiêu lần tùy ý cho hợp hoàn cảnh: đổi nhân vật, thêm không khí theo mùa, chuyển sang các ấn phẩm khác.

2.  Ngay cả một "ý niệm (mọi người tụ họp)" trừu tượng cũng có thể thành "hình hài (một logo)" qua nhiều lần trao đổi.

3.  Những việc tẻ nhạt (cắt ảnh) chính là thứ Gemini × Google Colab có thể tự động hóa. Lỗi thì giải quyết được bằng ảnh chụp màn hình.

#### Chuyên mục 1: Hướng dẫn nhập môn "Google Colab" cho chủ quán không rành kỹ thuật

~Hãy dùng một "căn bếp cho thuê" và cứ để nguyên máy tính của bạn~

"Google Colab" xuất hiện trong phần chính. Lập trình (Python) trên máy tính của mình giống như "nấu ramen chính gốc từ đầu, bắt đầu từ nước dùng, trong căn bếp ở nhà". Khâu chuẩn bị rất vất vả.

Còn Google Colab là "căn bếp cho thuê miễn phí, đầy đủ dụng cụ nấu nướng". Chỉ cần mở trình duyệt là những công cụ tốt nhất đã sẵn sàng. Bạn không cần đổi bất kỳ thiết lập nào trên máy tính. Bạn có thể lập trình chỉ bằng trình duyệt mà vẫn giữ môi trường máy gọn gàng. Trước hết, hãy tìm "Google Colab" và ghé nhìn căn bếp cho thuê này.

#### Chuyên mục 2: Không "đọc" màn hình lỗi mới là đáp án đúng

~Làm chủ vũ khí tối thượng: ảnh chụp màn hình~

Khi có lỗi hiện ra, bạn có đang nghiêm túc cố giải mã thông báo tiếng Anh không? Thế là phí thời gian.

Khi nêm nếm thấy vị hơi lạ lúc nấu, bạn nhờ đầu bếp nếm thử. Tương tự, hãy cứ cho AI xem một "ảnh chụp màn hình (screenshot)".

- Windows: \[Win\] + \[Shift\] + \[S\]

- Mac: \[Cmd\] + \[Shift\] + \[4\]\
  Bấm các phím này, kéo khung quanh phần lỗi rồi dán vào Gemini. Chỉ vậy thôi. Đừng "đọc lỗi", hãy "cho xem lỗi". Chỉ cần đổi cách nghĩ như thế, tốc độ phát triển hệ thống của bạn sẽ tăng gấp ba.

Tôi đã giới thiệu vài ví dụ cho đến giờ, và mọi việc tôi làm quy về ba điểm sau.

・Đừng đòi hình hài hoàn chỉnh ngay trong một lần (cứ coi như sẽ có đối thoại qua lại cũng được)\
・Cứ nói "không, chưa đúng lắm" mà đừng ngại\
・Coi như chi phí sửa lại bằng không và cứ tung yêu cầu ra một cách thoải mái

Bạn không cần tài năng thiết kế. Bạn chỉ cần dũng khí để nói thành lời điều "mình thấy vướng mắc".

## Chương 4: Thực hành phần 2 - Làm công việc hằng ngày hiệu quả hơn (dùng AI đa phương thức)

~Xong việc "nhập dữ liệu tẻ nhạt" chỉ bằng một chiếc điện thoại~

### 4-1. Nỗi phiền toái khi cập nhật danh sách rượu vang

Với chủ quán bar hay nhà hàng, cập nhật cuốn thực đơn là một gánh nặng không hào nhoáng nhưng rất nặng nề.

Điều khiến tôi đau đầu nhất là làm "danh sách rượu vang".

Mỗi lần có rượu vang mới về, tôi lại phải làm những việc sau.

1.  Nhìn nhãn chai (chữ nước ngoài viết bay bướm, rất khó đọc).

2.  Gõ tên nhãn hiệu và năm sản xuất (vintage) vào máy tính mà không để sai sót.

3.  Tra cứu đặc điểm và hương vị của chai rượu trên mạng.

4.  Viết một đoạn "giới thiệu" khiến khách muốn đọc.

5.  Nghĩ ra những món ăn hợp với chai rượu đó (pairing).

Vừa cầm từ điển vừa làm hết những việc này trong những khoảng trống giữa giờ phục vụ bận rộn gần như là bất khả thi. Tôi cứ trì hoãn với câu "để lúc khác làm", và danh sách gợi ý thường rốt cuộc chẳng bao giờ được cập nhật.

### 4-2. Chỉ cần chụp một tấm ảnh. Cú sốc mang tên "Gem danh sách rượu vang"

Thế là tôi quyết định thử "tính năng đa phương thức (nhận diện hình ảnh)" của Gemini.

Cách làm đơn giản đến mức không ngờ.

1.  Dùng điện thoại chụp ảnh chai rượu vang.

2.  Gửi tấm ảnh đó cho Gemini.

3.  Thêm một dòng: "Hãy lập thành danh sách."

Chỉ vậy thôi.

![Ảnh nhãn chai rượu vang thật chụp bằng điện thoại](images/fig-19.jpg)

Gemini lập tức đọc thông tin trên nhãn từ tấm ảnh.

Nó không chỉ chép lại tên nhãn hiệu, chẳng hạn "Cave d'Occi Winery, Tsukimi de Ippai 2024", mà còn tìm đặc điểm của chai rượu trong một cơ sở dữ liệu khổng lồ trên mạng và tự động viết ra một đoạn mô tả hấp dẫn.

Điều làm tôi ngạc nhiên hơn nữa là nó còn kèm theo cả "gợi ý kết hợp món ăn".

Những gợi ý như "Hương thơm đậm đà của chai rượu này rất hợp với ○○" hiện lên màn hình chỉ trong vài giây.

Những giờ vật lộn với cuốn từ điển ngày trước giờ gói gọn trong một lần bấm nút chụp trên điện thoại.

### 4-3. Tự tạo "Gem" của riêng mình

Để công việc này hiệu quả hơn hẳn, tôi tiếp tục dùng một tính năng gọi là "Gem".

Đó là "tính năng AI tùy chỉnh của riêng bạn", cho phép bạn để AI ghi nhớ trước một vai trò và các quy tắc nhất định.

Lần nào cũng phải giải thích từ đầu: "Bạn là một sommelier. Hãy nhìn bức ảnh này và..." thì thật phiền.

Vì vậy tôi đã đăng ký sẵn với Gemini những "chỉ dẫn (prompt)" sau. Đây chính là thứ bên trong đầu "AI sommelier chuyên trách" của quán bar tôi.

#### Chỉ dẫn mà tôi đang đăng ký thực tế

> Hãy đọc hình ảnh và tạo danh sách rượu vang theo định dạng sau.
>
> Về giá, đừng dùng giá thị trường. Hãy tính theo giá một chai ở nhà hàng thông thường (khoảng 2,5 đến 3 lần giá vốn).
>
> Đừng dùng dạng bảng. Hãy tạo sao cho vừa trong một hoặc hai tờ giấy A4.
>
> Định dạng chỉ để tham khảo; hãy lập danh sách chỉ với những gì đã được nhập vào.
>
> Định dạng như bên dưới.
>
> Vương quốc Anh 🇬🇧
>
>  Ridgeview Bloomsbury NV  ¥8.500 (khoảng $57)
>
>  Màu vàng nhạt với bọt khí dễ chịu. Thoang thoảng dưa lưới và mật ong giữa hương cam quýt... (phần còn lại được lược bỏ)

Thực ra, phần "định dạng (mẫu)" ở nửa dưới của prompt này:

Tôi không nghĩ ra nó từ con số không.

Trước đây, khi tìm thông tin về rượu vang trên mạng, tôi hay nghĩ "Ồ, phần mô tả của cửa hàng này dễ hiểu", hay "Trang này viết nghe thật ngon", rồi cứ thế sao chép những đoạn như vậy vào một cuốn sổ ghi chú trên máy, hết lần này đến lần khác.

Tôi đã ném nguyên cái "bản ghi chú chắp vá" đó cho Gemini.

"Đây là những đoạn tôi đã sao chép và gom lại từ trước. Hãy bắt chước văn phong này và viết về chai rượu trong bức ảnh mới nữa nhé."

Tôi chỉ nói với nó có thế.

Dù vậy, chỉ dẫn này vẫn chứa ba mẹo giúp giảm gánh nặng cho công việc ở quán.

① "Logic tính giá"

Đây là điểm tiết kiệm thời gian nhất. Vì tôi yêu cầu nó đưa ra "giá mà nhà hàng sẽ bán" thay vì "giá thị trường", AI sẽ tính ngược từ giá nhập thông thường và cho tôi một con số như "¥8.500 (khoảng $57)" có thể đưa thẳng lên thực đơn. (Tất nhiên, quyết định cuối cùng là của chủ quán, nhưng có một mức tham chiếu thì mọi việc dễ hơn.)

② "Không dùng dạng bảng, mà vừa trong tờ A4"

Nếu kết quả trả về ở dạng bảng như Excel, bố cục sẽ vỡ khi dán vào quyển thực đơn. Bằng cách yêu cầu nó viết theo "định dạng thực đơn A4" ngay từ đầu, tôi nhắm đến kết quả có thể in ra và dùng ngay.

③ Dùng văn bản sao chép từ web làm "mẫu"

Thay vì hỏi chung chung "Hãy viết một phần mô tả hay", tôi cho nó xem một ví dụ cụ thể (bản ghi chú sao chép của tôi): "cờ 🇬🇧 + tên rượu + giá + mô tả cảm quan (hương vị)".

Khi được cho xem một ví dụ, AI sẽ hiểu "À, ra đây là giọng điệu và cách viết mình cần theo", và độ chính xác của kết quả tăng vọt. Theo thuật ngữ kỹ thuật, đây gọi là "few-shot prompting", nhưng về bản chất nó giống như "dạy bằng cách để người ta nhìn theo bóng lưng mình".

Và "tấm lưng" đó hoàn toàn có thể là những "đoạn văn lượm lặt" trên mạng, giống như cách người ta lượm ảnh trên web vậy.

![Văn bản danh sách rượu vang hoàn chỉnh do Gemini tạo ra](images/fig-20.png)

### 4-4. Thậm chí không cần là hình ảnh. Cuộc cách mạng sao chép và dán từ LINE

Điều tuyệt vời ở "Gem danh sách rượu vang" này là đầu vào không chỉ giới hạn ở ảnh.

Thực tế, ở quán bar thì bạn thường đặt hàng với cửa hàng rượu qua LINE, đúng không?

Khi đặt hàng xong, cửa hàng rượu sẽ gửi về một tin nhắn như thế này.

> "Cảm ơn quý khách đã luôn ủng hộ. Chúng tôi đã nhận đơn hàng của quý khách như sau.
>
> ・Cave d'Occi Tsukimi de Ippai Blanc 24 3 chai
>
> ・Ridgeview Bloomsbury 6 chai
>
> ・○○ (rượu mới) 2 chai
>
> Ngày mai chúng tôi sẽ giao hàng."

Một hôm, tôi chợt nghĩ: "Mình có thể dùng nguyên văn bản này không nhỉ?"

Để thử, tôi dùng ngón tay sao chép tin nhắn LINE này rồi ném thẳng vào Gemini.

Kết quả hoàn hảo.

Gemini chỉ nhận ra "tên sản phẩm" trong tin nhắn LINE, tìm thông tin trên mạng, rồi lập danh sách theo định dạng quen thuộc (cờ + giá + mô tả).

Nói cách khác, tôi thậm chí không cần chờ rượu về để chụp ảnh.

Ngay lúc đặt hàng, chỉ bằng thao tác sao chép và dán ngay trong điện thoại, danh sách thực đơn đã xong trước cả khi hàng kịp đến.

Không cần mở máy tính, không cần bật máy ảnh.

Ở một góc bếp, hay trên tàu điện, công việc được hoàn tất chỉ bằng thao tác trên điện thoại.

Chẳng phải đây chính là "hiệu quả thực sự" mà một chủ quán một mình nên hướng tới sao?

### 4-5. Gợi ý của AI × Phán đoán thực tế tại quán (Thực tế)

Dù vậy, tôi không máy móc nghe theo mọi gợi ý của AI. Điều quan trọng ở đây là "phán đoán thực tế của con người tại quán" của chúng ta.

Có lần, AI đưa ra gợi ý này để đi cùng một chai rượu vang:

AI: "Với chai vang đỏ này, ức vịt áp chảo sốt cam là sự kết hợp hoàn hảo."

Một gợi ý tuyệt vời, nhưng tiếc là hôm đó trong tủ lạnh của quán không có thịt vịt.

Tôi không nghĩ "AI đã nói vậy nên mình phải đi mua vịt". Tôi nghĩ như thế này:

Tôi (tại quán): "Quán không có vịt, nhưng hôm nay có gà thả vườn ngon vừa về. Loại gà này có lượng mỡ không kém vịt, nên mình sẽ áp chảo cho da giòn rồi hoàn thiện bằng sốt vị cam, đúng như AI gợi ý."

"Kiến thức của AI (vịt và cam hợp nhau)" × "nguyên liệu có sẵn tại quán (quán có gà)" = "một món mới thực tế mà không cần đắn đo suy nghĩ".

Sự kết hợp này chính là niềm vui thực sự khi phát triển thực đơn cùng AI.

AI đưa cho bạn đáp án trong sách giáo khoa, nhưng nó không biết hôm nay trong tủ lạnh có gì. Lấp đầy khoảng trống đó là việc của bạn, với tư cách chủ quán.

### 4-6. Chặng cuối: AI không thể "nếm"

Còn một điều nữa mà bạn tuyệt đối không được giao cho AI.

Đó là việc nếm thử trước khi mang bất cứ thứ gì ra cho khách.

Những phần mô tả và gợi ý kết hợp món ăn mà AI viết dựa trên "dữ liệu phổ biến chung của số đông".

Nhưng rượu vang là một thực thể sống. Ngay cả cùng một nhãn, hương vị cũng thay đổi theo năm sản xuất và cách bảo quản.

Có lần, AI viết mô tả cho một chai vang trắng: "Một loại vang khô, tươi mát và nhẹ nhàng. Hoàn hảo với carpaccio hải sản."

Nhưng khi tôi thực sự mở chai ra nếm, nó đã chín muồi hơn tôi tưởng, với hương vị đậm đà như mật ong.

"Nếu mình giới thiệu đây là 'vang khô nhẹ nhàng', khách sẽ thất vọng mất... Nó hợp với gà sốt kem hơn là carpaccio."

Tôi sửa ngay đoạn văn Gemini đã tạo ra.

- Trước (AI): "Tươi mát và nhẹ nhàng. Hợp với món khai vị"

- Sau (con người): "Đậm đà, thân rượu đầy đặn nhờ quá trình ủ. Đủ mạnh để đi cùng món chính"

AI làm 90% bản nháp, còn con người nếm thử và thêm vào "10% cuối cùng (linh hồn)".

Việc kiểm tra này là trách nhiệm của người chủ nhà hàng, và là thứ AI không bao giờ bắt chước được.

Không phải "vì AI nói vậy", mà là "vì tôi đã uống và thấy ngon".

Để có thể phục vụ với sự tự tin đó, hôm nay tôi vẫn nếm chai rượu vừa mở, tay kia cầm danh sách do AI lập.

#### Chuyên mục 3: Mẹo chụp ảnh để AI nhìn "đúng"

~ Như đưa nhãn chai cho một sommelier xem ~

Khi gửi ảnh cho Gemini, vài mẹo nhỏ có thể cải thiện đáng kể khả năng nhận diện của nó.

1.  Tránh phản quang: Nhãn chai rất dễ phản chiếu ánh sáng, vì vậy hãy đổi góc chụp một chút, hoặc dùng bóng của cơ thể che bớt khi chụp.

2.  Chụp nhiều tấm và gửi cùng lúc: Với những thứ như đồ trong tủ lạnh, hãy gửi cả ảnh toàn cảnh lẫn ảnh cận cảnh, AI sẽ nhận ra cả những món nằm trong góc khuất.

3.  Chỉ bằng ngón tay: Chỉ vào chỗ bạn muốn AI nhìn khi chụp ảnh cũng rất hữu ích. Hãy đưa một câu như "Tôi đang chỉ bằng ngón tay" vào prompt. Cũng giống như chỉ vào thực đơn khi ở một nhà hàng nước ngoài.

## Chương 5: Ứng dụng - Phân tích kinh doanh và cải thiện lợi nhuận

~ Đào ra "mỏ vàng vô hình". Buổi họp quản lý cùng cố vấn AI của bạn ~

### 5-1. Những đêm vắt óc bên chiếc máy tính bỏ túi vào cuối mỗi tháng

Với những người làm chủ quán ăn nhỏ độc lập như chúng ta, không khoảng thời gian nào nặng nề bằng công việc chốt sổ hằng tháng.

Trong sự yên tĩnh đêm khuya, vừa tổng hợp dữ liệu máy tính tiền vừa nhập vào Excel, tất cả những gì bạn nghe thấy là tiếng thở dài của chính mình.

"Mục tiêu doanh thu tháng này là ○○0.000 yên. ...Mình đã không đạt."

"Số lượng khách cũng không tệ. Cuối tuần quán đông kín. Nhưng không hiểu sao mức chi tiêu bình quân mỗi khách lại không tăng."

Tại sao mình không đạt được mục tiêu? Món ăn hẳn là ngon. Mình cũng đang cố gắng hết sức trong phục vụ.

"Hay là giá quá cao?"

"Không, rẻ hơn nữa thì sẽ không có lãi. Mà giá nguyên liệu cũng đang tăng."

Những câu hỏi không có lời đáp cứ quanh quẩn trong đầu, và cuối cùng tôi lại kết thúc bằng lời tự động viên: "Tháng sau mình sẽ dồn thêm tinh thần và đẩy mạnh món gợi ý hơn nữa." Đây là thói quen xấu của tôi, và của rất nhiều chủ quán.

Nhưng giờ đây tôi có một cố vấn không có cảm xúc.

Tôi đối diện với Gemini cùng dữ liệu doanh thu của tháng đó và dữ liệu thực đơn của quán.

### 5-2. Một thí nghiệm: Cho AI đọc "hình ảnh" và "con số" cùng lúc

Lần này, tôi đưa cho Gemini ba nguồn thông tin.

Tôi ném vào, trộn lẫn tất cả, phần "thiết kế (não phải)" và "con số (não trái)" mà từ trước đến nay tôi vẫn quản lý riêng rẽ.

1.  "Mục tiêu doanh thu tháng này"

- Mong ước tha thiết của tôi. Con số nhất định phải đạt được.

2.  "Toàn bộ dữ liệu từ các phiếu bán hàng gần đây (CSV/Excel)"

- Kết quả trong thực tế. Sự thật lạnh lùng về ai đã gọi món gì, với mức giá nào.

3.  "Một tệp PDF của thực đơn hiện tại"

- Thế giới mà khách hàng nhìn thấy. Những thông tin trực quan như vị trí đặt ảnh, cỡ chữ và cách phối màu.

Và rồi tôi hỏi như thế này.

Đó không phải là một yêu cầu công việc như lần "tạo hình ảnh" trước. Đó là một câu hỏi, kiểu câu hỏi mà một chủ quán sẽ đặt ra.

> "Hãy so sánh dữ liệu doanh thu hiện tại (thực tế) với bố cục của thực đơn (diện mạo).
>
> Hãy chỉ ra điểm nghẽn: chúng ta đang thiếu điều gì để đạt mục tiêu ○○0.000 yên?"

### 5-3. "Định kiến của chủ quán" mà AI nhìn thấu

Vài giây sau, câu trả lời của Gemini quay lại, và nó đánh thẳng vào điểm mù của tôi.

Tôi đã đoán rằng mình sẽ nhận được những lời khuyên chung chung như "Hãy phát triển một món mới" hay "Hãy quảng bá trên mạng xã hội".

Nhưng điều AI chỉ ra lại là một sự thật mà tôi vẫn vô thức cố giấu đi.

Câu trả lời của Gemini:

> "Đối chiếu dữ liệu với thực đơn, tôi nhận thấy một cơ hội lớn đã bị bỏ lỡ.
>
> Gói uống thỏa thích (all-you-can-drink), vốn có biên lợi nhuận cao và có thể nâng chi tiêu bình quân mỗi khách một cách chắc chắn, hiện chỉ được ghi trên thực đơn (Before) bằng chữ, lặng lẽ ở góc dưới cùng bên trái.
>
> Trong khi đó, vị trí đẹp nhất trên thực đơn, ngay trên cùng, lại dành cho 'Set ¥2.200 (khoảng $15)' giá rẻ. Như vậy, khách hàng dễ trôi về gói rẻ hơn và thậm chí không hề nhận ra gói uống thỏa thích có giá cao hơn."

Nhìn màn hình, tôi không kìm được tiếng rên lên. Nó đúng từng chữ.

Quán tôi có gói uống thỏa thích. Nhưng đâu đó trong đầu, tôi đã luôn nghĩ như thế này:

"Quán mình không phải là izakaya chuỗi *(quán nhậu bình dân kiểu Nhật phục vụ cả đồ ăn lẫn đồ uống)*. Quảng cáo uống thỏa thích bằng chữ to trông rẻ tiền."

"Mình muốn mọi người thưởng thức hương vị của rượu vang, nên chỉ những ai biết đến nó mới gọi thôi."

"Định kiến" đó của tôi đã lộ ra trong bố cục thực đơn, ở dòng chữ dưới cùng.

![Thực đơn Before. Mục uống thỏa thích nằm ở góc dưới bên trái và không nổi bật. Cũng khó nhận ra rằng đồ ăn được tách riêng](images/fig-21.png)

AI đã không bỏ sót điều đó.

"Chủ quán ơi, bạn muốn đạt con số mục tiêu đúng không? Vậy thì hãy đặt gói mà bạn muốn bán nhất, gói có uống thỏa thích, ngay trên cùng một cách đầy tự hào."

### 5-4. Không có hình ảnh? Vậy cứ để AI vẽ luôn

Tôi quyết tâm. "Nếu chỉ vì trông ngầu mà doanh thu giảm thì mình sẽ thử, bằng mọi giá."

Nhưng đến đây lại nảy sinh một vấn đề.

"Dù có đặt thật to ở trên cùng, chỉ có chữ thì vẫn yếu..."

Còn nếu tôi lấy một tấm ảnh mọi người nâng cốc bia từ trang ảnh miễn phí, trông sẽ lập tức giống nhà hàng chuỗi. Nó không hợp với không khí quán của tôi.

Tôi không có tài vẽ, mà thuê họa sĩ minh họa thì tốn tiền và tốn thời gian.

Tôi bắt đầu lo "Phải làm sao đây...?" nhưng rồi lập tức nhớ ra.

"Đúng rồi, mình có một phó quản lý (AI) biết vẽ."

Tôi đã tìm được trên một trang tư liệu miễn phí một hình gần với ý tưởng của mình. Trang đó ghi là cho phép chỉnh sửa.

Tôi tiếp tục gõ vào khung trò chuyện như sau:

> "Hãy vẽ một hình minh họa để đặt ở phía trên cùng của thực đơn. Dựa trên hình đính kèm.
>
> Tôi muốn có cảm giác mọi người vui vẻ nâng ly, nhưng không được trông rẻ tiền.
>
> Hãy làm theo phong cách nét vẽ đơn giản."

Vài giây sau, bốn phương án minh họa hiện lên trên màn hình.

Trong số đó, tôi chọn hình minh họa "Cheers!" giản dị, ấm áp, hợp nhất với không khí của quán.

![Hình minh họa "Cheers!" do AI tạo ra chỉ trong 10 giây](images/fig-22.png)

Chỉ mất 10 giây.

Không chỉ phần phân tích: ngay cả "tư liệu" cần cho việc cải thiện cũng có thể kiếm được ngay tại chỗ.

Đây chính là sức mạnh thực sự của việc đưa AI tạo sinh vào quản lý kinh doanh.

### 5-5. Chỉ đổi bố cục mà chi tiêu bình quân mỗi khách tăng khoảng 40%

Thế là tôi thiết kế lại thực đơn.

#### Before: Thực đơn như cũ

- Vị trí đẹp nhất (trên cùng): Các món giá rẻ như "Set ¥2.200 (khoảng $15)" và "Set Course ¥3.300 (khoảng $22)."

- Uống thỏa thích: Chỉ được ghi bằng chữ ở góc dưới bên trái, dưới dạng "Uống thỏa thích từ ¥3.000 (khoảng $20)." Nó hoàn toàn bị chìm đi.

#### After: Thực đơn đã chỉnh sửa

- Vị trí đẹp nhất (trên cùng): Các gói giá cao từ ¥4.500–¥5.700 (khoảng $30–$38), được giới thiệu là "Lựa chọn hàng đầu của quán! Full Enjoyment Course (có uống thỏa thích)."

- Thiết kế: Với hình minh họa "Cheers!" do AI tạo ra được thêm vào, nó dẫn mắt người xem một cách mạnh mẽ, bằng hình ảnh, tới thông điệp "Hãy nhìn vào đây trước tiên."

- Thay đổi bố cục: Những set rẻ từng là ngôi sao trước đây được chuyển xuống phía dưới.

![Thực đơn After. Gói uống thỏa thích được đặt ở ngay trên cùng](images/fig-23.png)

Thực ra đồ ăn, giá cả và chất lượng đồ uống hầu như không thay đổi. Tất cả những gì tôi đổi chỉ là "cách trình bày" và "vị trí".

Còn kết quả?

Từ ngày hôm sau, hành vi gọi món của khách thay đổi đáng kể.

Những lời đầu tiên của khách khi mở thực đơn không còn là "Cứ cho bia trước đã", mà là "Vậy cho chúng tôi 'Top Pick Course (¥4.900 (khoảng $33))' có hình minh họa này."

Những khách trước đây thường kết thúc với "Set (¥2.200 (khoảng $15)) cộng hai ly" (mức chi khoảng ¥3.500 (khoảng $23) mỗi khách) giờ chọn ngay gói ¥4.900 (khoảng $33) từ đầu.

Chỉ riêng điều này đã khiến chi tiêu bình quân mỗi khách tăng vọt thêm ¥1.400 (khoảng $9,3).

Hơn nữa, khách còn được hưởng lợi ích "được uống mà không phải lo hóa đơn", nên mức độ hài lòng không giảm mà còn tăng.

### 5-6. Đối chiếu kết quả bằng tệp PDF doanh thu tháng 12 (PDCA)

Một tháng đã trôi qua kể từ khi tôi đưa biện pháp này vào thực hiện.

Không dừng lại ở đây chính là cốt lõi của việc dùng AI.

Nhiều chủ quán đánh giá kết quả theo cảm tính rồi thôi: "Đông khách nên chắc là hiệu quả", hay "Doanh thu tăng rồi, vậy là tốt".

Nhưng tôi lại đối diện với Gemini một lần nữa.

Lần này tôi tải lên "tệp PDF dữ liệu doanh thu tháng 12", nơi đã có kết quả, và hỏi như sau:

> "Kết quả của biện pháp tháng trước (thay đổi thực đơn) đã có.
>
> Hãy xem dữ liệu doanh thu tháng 12 này và đối chiếu kết quả (đánh giá): số lượng đơn 'Top Pick Course' có tăng như dự định không, và nó ảnh hưởng thế nào đến chi tiêu bình quân mỗi khách?"

Gemini phân tích dữ liệu ngay lập tức và gửi lại cho tôi một báo cáo.

![Màn hình báo cáo phân tích doanh thu của Gemini: tôi đã làm một bản tóm tắt để công bố, nên nội dung có phần khác với văn bản bên dưới](images/fig-24.png)

Phân tích của Gemini:

> "Đây là những kết quả xuất sắc. Nhìn vào xu hướng của dữ liệu, số lượng đơn 'Full Enjoyment Course' đã tăng lên khoảng 1,8 lần so với tháng trước.
>
> Kết quả là chi tiêu bình quân mỗi khách nói chung tăng trung bình ○○ yên.
>
> Nguyên nhân chính là việc đặt gói uống thỏa thích ở vị trí cao hơn đã làm tăng giá trị đơn hàng, đặc biệt ở các nhóm khách."

Nghe những lời đó, lần đầu tiên tôi cảm thấy thật sự yên tâm.

Không phải "bằng cách nào đó mà kiếm được tiền", mà là sự tự tin của "tôi đã nhắm tới và đã làm ra con số".

Điều này trở thành động lực cho biện pháp tiếp theo.

1.  Plan: Xem dữ liệu doanh thu và thực đơn, tìm ra vấn đề (gói uống thỏa thích đang bị giấu đi).

2.  Do: Nhờ AI vẽ minh họa và thay đổi bố cục thực đơn.

3.  Check: Cho nó đọc PDF doanh thu tháng 12 và kiểm chứng kết quả.

4.  Act: Cân nhắc xem xét lại bố cục thực đơn đồ ăn trong lần tới.

"Chu trình PDCA" mà các công ty lớn vận hành với chi phí khổng lồ, một chủ quán cá nhân như tôi cũng có thể vận hành chỉ với một chiếc điện thoại thông minh, nếu có AI làm đối tác.

## Chương 6: Thử thách - Phát triển một hệ thống chỉ dành riêng cho quán của mình

~ "Chưa có thì tự xây." Một dự án phát triển hệ thống không có chuyên gia ~

※Xin nói trước, bạn không cần làm hết mọi thứ trong cuốn sách này.

・Gửi một hình ảnh và nhờ AI viết chữ\
・Biến một tin nhắn LINE dài thành sơ đồ

Chỉ hai việc này là đủ để bắt đầu. Chỉ vậy thôi cũng chắc chắn sẽ giúp công việc của bạn nhẹ nhàng hơn.\
Chỉ cần đọc cuốn sách này như một câu chuyện và nghĩ "À, hóa ra với AI có thể làm được đến mức này" cũng đã đủ.

### 6-1. Ứng dụng làm sẵn không gãi đúng chỗ tôi "ngứa"

Cho đến giờ tôi đã nói về việc dùng AI trên các nền tảng có sẵn, như tạo hình ảnh và phân tích thực đơn.

Nhưng khi tiếp tục kinh doanh, sẽ nảy sinh những nỗi lo mà "ứng dụng làm sẵn" đơn giản là không giải quyết được.

Đặc biệt với một mô hình kinh doanh không theo khuôn mẫu như của chúng tôi, "bán cà ri ban ngày, mở bar ban đêm", dòng tiền vào ra cũng phức tạp.

"Tôi muốn đối chiếu số dư PayPay Bank với các khoản sắp phải thanh toán để biết số tiền còn lại vào cuối tháng."

"Ngày thanh toán chia ra ngày 10 và ngày 25. Tôi muốn mô phỏng điều đó."

Phần mềm kế toán trên thị trường rất mạnh, nhưng không cái nào nhắm đúng "nỗi lo đang có trong đầu tôi lúc này".

Vì vậy tôi quyết định.

"Chưa có thì mình tự xây. Mình có Gemini, kỹ sư giỏi nhất."

### 6-2. Giai đoạn 1-3: Từ những ghi chú nguệch ngoạc đến "đám mây"

Việc phát triển bắt đầu bằng việc cho Gemini xem các ghi chú của tôi trong Google Keep.

![Ghi chú Keep là điểm khởi đầu của việc phát triển](images/fig-25.png)

#### Giai đoạn 1: Xây dựng logic

"Tôi muốn tự động hóa các phép tính trong ghi chú này."

Đáp lại yêu cầu của tôi, Gemini nhanh chóng soạn ra logic tính toán.

- Khi tôi đổi số tiền của một khoản, nó tính ngay số dư cuối cùng.

- Nếu quỹ sắp thiếu, nó hiển thị "cảnh báo" bằng màu đỏ.

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

Nhưng tôi đã hiểu rằng việc mang theo "cây gậy phép (hiểu biết)" và "tấm khiên (biện pháp bảo mật)" để dùng thứ phép thuật đó cũng là một phần công việc của chủ quán từ nay về sau.

### 6-6. "Trách nhiệm" và "bảo hiểm" đi kèm với tự do

#### Quan trọng: Quyền riêng tư và thông tin cá nhân

"Hệ thống nhận diện khuôn mặt" này là một bản mẫu thử nghiệm tôi xây dựng để kiểm tra điều gì khả thi về mặt kỹ thuật. Nếu dùng nó ở một quán thật, dữ liệu khuôn mặt của khách sẽ được xem là "thông tin cá nhân (dữ liệu sinh trắc học)", và phải được bảo vệ nghiêm ngặt theo pháp luật (Luật Bảo vệ Thông tin Cá nhân của Nhật Bản).

Nếu bạn đang nghĩ đến việc áp dụng một thứ như thế này, xin nhất định ghi nhớ hai điểm sau.

Thông báo cho khách và xin sự đồng ý: Bạn cần có quy trình, chẳng hạn dán biển ở lối vào ghi "Chúng tôi sử dụng nhận diện khuôn mặt bằng AI" và xin sự đồng ý khi khách đăng ký thành viên. Quay lén tuyệt đối không được phép.

Bảo vệ dữ liệu: Bạn cần có các biện pháp đưa nguy cơ rò rỉ về mức bằng không, chẳng hạn quản lý dữ liệu trong một môi trường tách biệt khỏi internet.

Làm được không đồng nghĩa với được phép làm. Nếu bạn là chủ quán có kỹ năng kỹ thuật, xin hãy nhớ rằng trách nhiệm khi sử dụng công nghệ đó luôn đi kèm.

Đến giờ tôi mới chỉ nói về việc một hệ thống tự làm tuyệt vời đến mức nào. Nhưng với tư cách chủ doanh nghiệp, tôi cũng phải nói với bạn về một thực tế khắc nghiệt.

Đó là: "Mọi thứ bạn tự xây đều là trách nhiệm của chính bạn."

Với dịch vụ thuê bao hằng tháng (SaaS), nếu máy chủ gặp sự cố, công ty sẽ xin lỗi và đưa nó chạy lại.

Nhưng một hệ thống xây bằng vibe coding thì không có "bộ phận hỗ trợ khách hàng".

Nếu ứng dụng của bạn đột nhiên ngừng chạy vào giờ cao điểm buổi trưa, sẽ chẳng ai đến giúp.

Khi Google thay đổi một đặc tả, chuyện mã nguồn hôm qua còn chạy tốt mà hôm nay báo lỗi là điều xảy ra thường ngày.

Vì vậy tôi có hai sự chuẩn bị.

Một là "bản dự phòng analog".

"Nếu nhận diện khuôn mặt ngừng hoạt động, hãy xem sổ khách hàng bằng giấy." "Nếu ứng dụng máy tính tiền hỏng, hãy dùng máy tính bỏ túi và phiếu viết tay."

Công cụ kỹ thuật số chỉ là "công cụ tiện lợi". Bạn không được phụ thuộc vào chúng đến mức khi chúng dừng lại thì quán của bạn cũng dừng theo.

Hai là "bảo hiểm" mà tôi đã nhắc ở trên.

Bảo hiểm trách nhiệm rủi ro mạng không chỉ bao gồm rủi ro rò rỉ thông tin, mà còn cả khoản bồi thường cho thiệt hại kinh doanh khi lỗi của chính bạn làm hệ thống ngừng hoạt động. Với một chủ quán cá nhân đang trang bị IT cho mình, đó là một phần của việc làm người trưởng thành có trách nhiệm.

"Đôi khi mọi thứ sẽ ngừng chạy. Đôi khi tôi sẽ mắc lỗi."

Hãy coi đó là điều hiển nhiên, chấp nhận rủi ro và có biện pháp ứng phó.

Chỉ khi có quyết tâm này, chúng ta mới thực sự dùng được một "hệ thống tự do" không bị ràng buộc bởi bất kỳ ai.

### 6-7. Bạn không cần chuyên gia. Bạn cần sự kiên trì

Tôi đã không trả một yên phí thuê ngoài nào cho việc phát triển hai hệ thống này.

Tất cả những gì tôi dùng là một gói thuê bao AI vài nghìn yên mỗi tháng, và sự kiên trì của một chủ quán nghĩ rằng "Nhất định phải xóa bỏ nỗi lo này (về dòng tiền)" và "Tôi muốn làm khách hàng vui".

Đây không phải chuyện "Tôi không làm được vì tôi không biết lập trình".

Nếu có điều bạn muốn xây dựng (Want), AI sẽ dạy bạn cách xây dựng nó (How).

Ngay cả khi xuất hiện những từ bạn không hiểu (Node.js, PowerShell, Firestore...), cũng chẳng có gì phải sợ.

Chúng ta có người đồng hành mạnh nhất có thể có, "Gemini", để dịch chúng và dẫn đường cho chúng ta.

#### Chuyên mục 4: Excel và cơ sở dữ liệu (Firestore) khác nhau ở đâu?

~ Là "ghi chú để bạn đọc", hay "sổ cái để hệ thống đọc"? ~

Firebase (Firestore) đã xuất hiện trong quá trình phát triển ứng dụng dòng tiền. Có thể bạn đã tự hỏi, tại sao không dùng Excel?

Bảng tính (Excel) là "cuốn sổ để con người nhìn và gõ vào". Nó rất linh hoạt, nhưng với một hệ thống thì nó mơ hồ về việc "cái gì nằm ở đâu".

Ngược lại, cơ sở dữ liệu (Firestore) là "một tủ khóa được sắp xếp gọn gàng, làm ra cho hệ thống". Vì đã cố định rằng "ngày nằm ở ngăn 1 và số tiền ở ngăn 2", chương trình có thể xử lý ngay lập tức. Nó cũng không bị hỏng khi nhiều người truy cập cùng lúc.

"Nếu bạn đang xây một ứng dụng, hãy dùng cơ sở dữ liệu, đừng dùng Excel." Chỉ cần biết điều này cũng sẽ nâng chất lượng các chỉ dẫn của bạn cho AI lên một bậc.

## Lời kết: Một "công thức cho tương lai" chỉ riêng quán của bạn có

~ AI không phải là một công nghệ khó. Nó là một người bạn đồng hành mới để "trò chuyện" ~

Cảm ơn bạn đã đọc cuốn sách này đến tận cùng.

Nếu chỉ thử một điều từ cuốn sách này, hãy thử điều này: "Dán nguyên tin nhắn LINE phiền phức đó vào AI và nhờ nó 'biến thành sơ đồ'."

Tôi không phải một chuyên gia AI đặc biệt. Tôi chỉ đơn giản lặp lại mỗi ngày việc "nói chuyện với AI bằng ngôn ngữ của nơi làm việc", \
trên chiến trường của một nhà hàng.

Vì vậy tôi nghĩ chỉ cần bạn mang về từ cuốn sách này không phải một "bộ sưu tập đáp án đúng", mà chỉ một "cách nghĩ" là đủ.

Khi mở trang đầu tiên, bạn đã hình dung thế nào về cụm từ "dùng AI"?

"Nghe có vẻ khó." "Phải có kiến thức lập trình chứ?" "Chẳng liên quan gì đến một quán nhỏ như của mình."

Có thể bạn đã nghĩ những điều như thế.

Nhưng giờ đây, khi đã đọc đến đây bản ghi chép về quá trình "thử và sai" của tôi, có lẽ hình dung đó đã thay đổi đôi chút.

Điều tôi làm không phải là tận dụng triệt để công nghệ IT tiên tiến.

Tôi càu nhàu: "Cái này làm bằng tay không nổi." Tôi phàn nàn: "Cái này khó dùng quá." Và tôi cứ đòi hỏi: "Tôi muốn nó chạy giống thế này hơn."

Dạo gần đây, trong giới kỹ sư, thuật ngữ "vibe coding" đang là xu hướng.

Đó là phương pháp xây dựng hệ thống theo cảm giác, trong khi trò chuyện với AI.

Giống như người chơi cờ shogi trò chuyện với AI để đọc các nước đi tiếp theo, chúng ta cũng có thể trò chuyện với AI và xây dựng "tương lai của quán mình".

Giống như bảo nhân viên bếp: "Nêm thêm chút muối nhé."

Giống như hỏi người bán cá ở chợ: "Hôm nay có cá nào ngon không?"

Nói với AI rằng "Hãy làm cho việc này nhẹ nhàng hơn." Mọi thứ bắt đầu từ đó.

Tôi từng làm ở bộ phận hệ thống của một công ty, đóng vai trò điều phối giữa "nơi vận hành" và "các nhà phát triển".

Giờ đây tôi đang làm đúng việc đó giữa "quán của mình" và "AI".

Và tôi tin chắc điều này:

"Một chủ quán hiểu những rắc rối trong vận hành thực tế có thể trở thành người chỉ huy AI mạnh nhất."

Bạn cũng hãy bắt đầu ngay hôm nay.

Trước hết, hãy lấy điện thoại ra và trò chuyện với Gemini.

"Này, hôm nay chuẩn bị nguyên liệu nên bắt đầu từ đâu?"

"Làm sao để món này bán chạy hơn?"

"Đống giấy tờ này phiền quá. Bạn có làm gì được không?"

Đừng lo nếu có lỗi xuất hiện. Đó là dấu hiệu cho thấy "cuộc trò chuyện" đã bắt đầu.

Chỉ cần chụp màn hình và gửi lại kèm câu "có gì đó sai sai".

Ở cuối chuỗi những cuộc trò chuyện chồng chất ấy, đang chờ bạn là "thời gian" và "sự thong thả" mà bạn không thể tưởng tượng nổi, cùng "một tương lai chỉ thuộc về quán của bạn".

Nào, hãy thuê một "phó quản lý" đáng tin cậy cho quán của bạn nữa.

Bởi công thức cho tương lai sẽ được sinh ra từ cuộc trò chuyện giữa bạn và AI.

### Ba lối ra của cuốn sách này

Cuốn sách này được đọc miễn phí dưới dạng PDF, trên note và trên Google Play. (Chỉ riêng Kindle, quy định của cửa hàng yêu cầu phải có giá tối thiểu.) Đổi lại, tôi đã chuẩn bị ba nơi bạn có thể ghé sau khi đọc xong. Chỉ cần bạn dùng dù chỉ một trong số đó, việc viết cuốn sách này đã xứng đáng.

1. Thử ngay tại quán của bạn. Loạt Agenda có thể bắt đầu bằng một cuốn sổ miễn phí. https://bontallc.com/agenda?via=b1-vi-{{FMT}}
2. Theo dõi những gì tôi làm. Tôi viết về những công cụ tôi sẽ làm tiếp theo và về cuộc sống thường ngày ở quán bar, trên note và X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Nếu có dịp đến Tokyo, hãy ghé Tamuro. Cách cửa đông ga Higashi-Nakano một phút. Bạn có thể vào mà không cần đặt chỗ. Khi cuốn sách này được viết lần đầu, Tamuro chỉ nhận khách qua giới thiệu. Ngày nay ai cũng được chào đón vào quán, không cần đặt chỗ. Trang đặt chỗ https://tamuroreservation.vercel.app/?src=b1-vi-{{FMT}}

Gửi đến những ai đến quán nhờ cuốn sách này: khi đặt chỗ, xin hãy nhập mã giảm giá "BOOK". Chúng tôi sẽ mời bạn một ly đồ uống trong lần ghé đầu tiên. Nếu bạn đến mà không đặt chỗ, chỉ cần nói "Tôi thấy trong sách" khi gọi món đầu tiên. Chúng tôi sẽ mời bạn đúng ly đồ uống đó. Đây là một cách nhỏ để tôi đếm được có bao nhiêu người đến nhờ cuốn sách.

### Về tác giả

Raku Bonta

Một chủ quán một mình điều hành nhà hàng có 11 chỗ ngồi quầy và 8 chỗ ngồi phòng tatami ở Higashi-Nakano, Tokyo.

Ban ngày là quán cà ri hamburger thơm mùi gia vị. Ban đêm là quán bar ăn uống chỉ nhận khách qua giới thiệu, phục vụ set ăn thay đổi mỗi ngày.

▼ Quatre Epice Hamburger Curry

https://www.instagram.com/quatre.epice.hamburg.curry/

![Cà ri hamburger Quatre Epice](images/fig-28.png)

▼ Quán bar chỉ nhận khách qua giới thiệu "Tamuro"

https://www.instagram.com/tamuro.higashinakano/

![Quán bar chỉ nhận khách qua giới thiệu "Tamuro"](images/fig-29.png)

Quán cũng dồn tâm sức xây dựng cộng đồng qua ẩm thực, với các sự kiện rượu vang hai tuần một lần, lớp học nấu ăn hằng tháng và các bữa tối nhiều món.

Trước khi tự mở quán cách đây 12 năm, tác giả từng làm tại một công ty ở mảng "hoạch định hệ thống" và "kiến trúc giải pháp".

Các chức danh nghe có vẻ khó, nhưng công việc thực chất là "một người điều phối truyền đạt chính xác mong muốn 'chúng tôi muốn làm thế này' của người làm việc trực tiếp tới các nhà cung cấp IT và nhờ họ xây dựng nên". Không phải một kỹ sư lập trình nâng cao, tác giả có sự nghiệp của một "người phiên dịch" kết nối con người với công nghệ.

Ngày nay, dựa trên kinh nghiệm đó, tác giả dùng AI tạo sinh như Google Gemini để vận hành quán của mình, thực hành và chia sẻ "cải tiến cách làm việc hiệu quả ngay cả khi không có chút kiến thức chuyên môn nào".
