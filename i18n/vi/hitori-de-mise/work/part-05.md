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

