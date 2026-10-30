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

