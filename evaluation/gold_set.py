"""
gold_set.py
-----------
Bộ câu hỏi-đáp án mẫu để đánh giá hệ thống RAG.

Mỗi mục gồm:
- question: câu hỏi đầu vào
- ground_truth: câu trả lời CHUẨN do con người soạn (dùng để chấm)
- (tuỳ chọn) reference_contexts: đoạn tài liệu gốc chứa đáp án

Quy mô khuyến nghị: 30-50 câu cho dự án nhỏ. Ở đây mình để 20 câu mẫu
trải đều các chủ đề (tiết kiệm, biểu phí, FAQ) và có CẢ câu mà tài liệu
không có đáp án — để kiểm tra hệ thống có "biết nói không biết" hay không.
"""

GOLD_SET = [
    # ---- Nhóm 1: Khái niệm & Quy định chung về TKTT ----
    {
        "question": "Trạng thái tài khoản 'ngủ' (Dormant) được xác định như thế nào?",
        "ground_truth": "Tài khoản thanh toán (TKTT) bị chuyển sang trạng thái ngủ khi không phát sinh giao dịch tài chính chủ động từ phía khách hàng trong thời gian từ 01 năm trở lên, ngoại trừ các giao dịch do hệ thống VietinBank tự động thực hiện.",
        "reference_contexts": "Bản điều khoản điều kiện về mở, sử dụng TKTT - Mục II.2.a.(i)"
    },
    {
        "question": "Người dưới 15 tuổi có được tự mình sử dụng tài khoản thanh toán không?",
        "ground_truth": "Không. Việc sử dụng TKTT của cá nhân chưa đủ 15 tuổi phải được thực hiện thông qua người giám hộ hoặc người đại diện theo pháp luật.",
        "reference_contexts": "Bản điều khoản điều kiện về mở, sử dụng TKTT - Mục II.1.b"
    },
    {
        "question": "VietinBank có quyền đóng tài khoản thanh toán của khách hàng trong trường hợp nào?",
        "ground_truth": "VietinBank có quyền đóng TKTT khi: khách hàng yêu cầu và đã thực hiện đủ nghĩa vụ; chủ TK chết/mất tích; tổ chức chấm dứt hoạt động; khách hàng vi phạm hành vi bị cấm; phát hiện giấy tờ giả mạo; hoặc TK có số dư bằng 0 và không hoạt động trên 01 năm.",
        "reference_contexts": "Bản điều khoản điều kiện về mở, sử dụng TKTT - Mục II.2.d"
    },

    # ---- Nhóm 2: Biểu phí Thẻ Ghi nợ (Nội địa & Quốc tế) ----
    {
        "question": "Phí phát hành lần đầu cho thẻ ghi nợ nội địa Chip contactless Epartner là bao nhiêu?",
        "ground_truth": "Phí phát hành lần đầu cho thẻ Chip contactless Epartner và Epartner liên kết VCCS được miễn phí.",
        "reference_contexts": "Biểu phí thẻ Ghi nợ nội địa cá nhân - Mã phí C001"
    },
    {
        "question": "Phí rút tiền mặt tại ATM VietinBank đối với thẻ Ghi nợ nội địa thông thường là bao nhiêu?",
        "ground_truth": "Phí là 1.000 đ/giao dịch (áp dụng cho thẻ Epartner thông thường, thẻ S-Card, thẻ C-Card...). Riêng thẻ Premium, thẻ G, thẻ Pink là 2.000 đ.",
        "reference_contexts": "Biểu phí thẻ Ghi nợ nội địa cá nhân - Mã phí C042"
    },
    {
        "question": "Thẻ ghi nợ quốc tế Visa Debit Platinum Sống khỏe có phí thường niên là bao nhiêu?",
        "ground_truth": "Phí thường niên đối với thẻ chính Visa Debit Platinum Sống khỏe là 163.636 đ.",
        "reference_contexts": "Biểu phí thẻ Ghi nợ quốc tế cá nhân - Trang 3"
    },
    {
        "question": "Phí vấn tin tài khoản và in sao kê tại ATM VietinBank cho thẻ ghi nợ nội địa là bao nhiêu?",
        "ground_truth": "Dịch vụ vấn tin và in sao kê giao dịch tại ATM VietinBank cho thẻ ghi nợ nội địa được miễn phí.",
        "reference_contexts": "Biểu phí thẻ Ghi nợ nội địa cá nhân - Mã phí C075"
    },

    # ---- Nhóm 3: Biểu phí Thẻ Tín dụng (Nội địa & Quốc tế) ----
    {
        "question": "Lãi suất áp dụng cho thẻ tín dụng quốc tế cá nhân tại VietinBank là bao nhiêu?",
        "ground_truth": "Lãi suất thẻ tín dụng quốc tế là 22%/năm.",
        "reference_contexts": "Biểu phí thẻ Tín dụng quốc tế cá nhân - Trang 10"
    },
    {
        "question": "Hạn mức rút tiền mặt tối đa của thẻ tín dụng quốc tế trong 01 tháng là bao nhiêu?",
        "ground_truth": "Tổng hạn mức rút tiền mặt tính theo BIN của thẻ tín dụng tối đa là 100.000.000 đ (một trăm triệu đồng) trong 01 tháng.",
        "reference_contexts": "Điều khoản & Điều kiện phát hành sử dụng thẻ tín dụng - Điều 5.3"
    },
    {
        "question": "Thẻ tín dụng nội địa i-Zero có phí thường niên là bao nhiêu?",
        "ground_truth": "Phí thường niên của thẻ tín dụng nội địa i-Zero là 299.000 đ.",
        "reference_contexts": "Biểu phí thẻ Tín dụng nội địa cá nhân - Mã phí C815"
    },
    {
        "question": "Mức phí phạt chậm thanh toán cho thẻ tín dụng quốc tế Visa Signature là bao nhiêu?",
        "ground_truth": "Nợ quá hạn dưới 30 ngày: 3% (tối thiểu 200.000 đ). Nợ quá hạn từ 30-60 ngày: 4% (tối thiểu 200.000 đ).",
        "reference_contexts": "Biểu phí thẻ Tín dụng quốc tế cá nhân - Mã phí C455, C456"
    },

    # ---- Nhóm 4: Thẻ kép 2Card & Tài khoản số đẹp ----
    {
        "question": "Phí thường niên của dòng thẻ Credit trong bộ thẻ kép 2Card là bao nhiêu?",
        "ground_truth": "Phí thường niên cho thẻ Credit 2Card là 199.000 đ.",
        "reference_contexts": "Biểu phí thẻ kép nội địa 2Card - Mã phí C815"
    },
    {
        "question": "Phí mở tài khoản thanh toán số đẹp 3 chữ số 'Lộc Phát' là bao nhiêu?",
        "ground_truth": "Mức phí tối thiểu để mở TKTT 3 chữ số 'Số giống nhau, Lộc phát' là 2.000.000 đ.",
        "reference_contexts": "Biểu phí dịch vụ tài khoản theo yêu cầu - Mã phí A004"
    },
    {
        "question": "Phí mở tài khoản số đẹp 12 ký tự theo ngày sinh (số tự chọn đến 6 chữ số) là bao nhiêu?",
        "ground_truth": "Phí mở tài khoản theo yêu cầu với số tự chọn đến 6 chữ số là 1.000.000 đ.",
        "reference_contexts": "Biểu phí dịch vụ tài khoản theo yêu cầu - Mã phí A034"
    },

    # ---- Nhóm 5: Dịch vụ Chuyển tiền & Khác ----
    {
        "question": "Phí chuyển tiền VND tại quầy cùng hệ thống nhưng khác tỉnh/TP là bao nhiêu?",
        "ground_truth": "Mức phí là 0,01% giá trị giao dịch (Tối thiểu: 10.000 đ; Tối đa: 1.000.000 đ).",
        "reference_contexts": "Dịch vụ thanh toán chuyển tiền - Mục 1.1 (Mã phí A101)"
    },
    {
        "question": "Phí dịch vụ Alias (đặt tên cho tài khoản) bằng số điện thoại là bao nhiêu?",
        "ground_truth": "Phí đăng ký Alias là số điện thoại hoặc gợi ý là 1.000.000 đ/Alias.",
        "reference_contexts": "Biểu phí dịch vụ tài khoản thanh toán - Mã phí A410"
    },
    {
        "question": "VietinBank thu phí bao nhiêu khi khách hàng nộp tiền mặt ngoại tệ (USD) vào tài khoản cùng tỉnh?",
        "ground_truth": "Nếu nộp USD mệnh giá <= 20 đơn vị: phí 0,5% (tối thiểu 50.000 đ). Nếu mệnh giá > 20 đơn vị: Miễn phí.",
        "reference_contexts": "Biểu phí dịch vụ tài khoản thanh toán - Mã phí A033"
    },
    {
        "question": "Điện phí (SWIFT) khi chuyển tiền ngoại tệ ra nước ngoài là bao nhiêu?",
        "ground_truth": "Điện phí SWIFT cho giao dịch chuyển tiền ngoại tệ ra nước ngoài là 5 USD.",
        "reference_contexts": "Dịch vụ thanh toán chuyển tiền - Mã phí A172"
    },

    # ---- Nhóm 6: Câu hỏi tình huống (FAQ) ----
    {
        "question": "Tôi bị mất thẻ tín dụng thì phải làm gì đầu tiên?",
        "ground_truth": "Khách hàng phải chủ động khóa thẻ ngay trên ứng dụng VietinBank iPay/eFast hoặc gọi tổng đài 24/7 của ngân hàng để thông báo và yêu cầu khóa thẻ.",
        "reference_contexts": "Điều khoản & Điều kiện phát hành sử dụng thẻ tín dụng - Điều 2.2.q"
    },
    {
        "question": "Nếu tôi không đồng ý với các thay đổi về biểu phí của VietinBank thì sao?",
        "ground_truth": "Nếu không đồng ý với nội dung sửa đổi, khách hàng có quyền thực hiện thủ tục chấm dứt sử dụng dịch vụ/đóng tài khoản theo quy định.",
        "reference_contexts": "Bản điều khoản điều kiện về mở, sử dụng TKTT - Mục IV"
    },
    {
        "question": "Tôi muốn cấp lại mã PIN cho thẻ ghi nợ nội địa tại quầy thì phí là bao nhiêu?",
        "ground_truth": "Phí cấp lại mã PIN tại quầy cho thẻ ghi nợ nội địa là 10.000 đ.",
        "reference_contexts": "Biểu phí thẻ Ghi nợ nội địa cá nhân - Mục Cấp lại mã PIN"
    },
    {
        "question": "Thẻ tín dụng quốc tế Mastercard Platinum Sendo có phí thường niên bao nhiêu?",
        "ground_truth": "Phí thường niên cho thẻ chính Mastercard Platinum Sendo là 399.000 đ.",
        "reference_contexts": "Biểu phí thẻ Tín dụng quốc tế cá nhân - Trang 4"
    },

    # ---- Nhóm 7: Câu hỏi kiểm tra 'Không có đáp án' (Testing Out-of-scope) ----
    {
        "question": "Lãi suất tiền gửi tiết kiệm bậc thang kỳ hạn 6 tháng hiện nay là bao nhiêu?",
        "ground_truth": "Rất tiếc, các tài liệu hiện tại chỉ cung cấp thông tin về biểu phí dịch vụ và điều khoản mở tài khoản thanh toán, không bao gồm bảng lãi suất tiền gửi tiết kiệm kỳ hạn cụ thể.",
        "reference_contexts": "None"
    },
    {
        "question": "VietinBank có hỗ trợ mở thẻ tín dụng bằng tài sản bảo đảm là bất động sản không?",
        "ground_truth": "Tài liệu này không đề cập chi tiết đến các loại tài sản bảo đảm cụ thể được chấp nhận để cấp hạn mức thẻ tín dụng (như bất động sản), chỉ nêu các quy định chung về xử lý tài sản bảo đảm khi có nợ quá hạn.",
        "reference_contexts": "None"
    },
    {
        "question": "Địa chỉ các phòng giao dịch của VietinBank tại Hà Nội là ở đâu?",
        "ground_truth": "Thông tin về danh sách địa chỉ các chi nhánh hoặc phòng giao dịch cụ thể không có trong các tài liệu biểu phí và điều khoản này.",
        "reference_contexts": "None"
    },
    # ---- Nhóm 8: Tiền gửi tiết kiệm (TGTK) & Tiền gửi có kỳ hạn (TGCKH) ----
    {
        "question": "VietinBank nhận tiền gửi tiết kiệm và tiền gửi có kỳ hạn bằng những loại đồng tiền nào?",
        "ground_truth": "VietinBank nhận tiền gửi bằng các loại đồng tiền: VND, USD, EUR.",
        "reference_contexts": "Quy định TGCKH dành cho KHCN - Mục I; Quy định TGTK - Mục 1."
    },
    {
        "question": "Nếu đến ngày đến hạn TGTK mà khách hàng không đến lĩnh và không có thỏa thuận khác, VietinBank sẽ xử lý như thế nào?",
        "ground_truth": "VietinBank sẽ tự động kéo dài thêm một kỳ hạn mới bằng kỳ hạn cũ. Nếu kỳ hạn đó không còn huy động, sẽ chuyển sang kỳ hạn thấp hơn liền kề.",
        "reference_contexts": "Quy định TGTK tại VietinBank - Mục 2.5"
    },
    {
        "question": "Khách hàng có thể tra cứu thông tin tiền gửi tiết kiệm qua những kênh nào?",
        "ground_truth": "Khách hàng có thể tra cứu qua: Xác nhận tại quầy giao dịch, VietinBank iPay/máy ATM, website www.vietinbank.vn, Tổng đài hỗ trợ khách hàng, hoặc qua dịch vụ thông báo biến động số dư SMS.",
        "reference_contexts": "Quy định TGTK tại VietinBank - Mục 4"
    },
    {
        "question": "Việc chuyển giao quyền sở hữu TGTK có bị giới hạn số lần không?",
        "ground_truth": "Không. Số dư TGTK không bị phong tỏa được phép chuyển giao quyền sở hữu không giới hạn số lần theo yêu cầu của người nhận thừa kế.",
        "reference_contexts": "Quy định TGTK tại VietinBank - Mục 2.4"
    },
    {
        "question": "Tiền gửi tiết kiệm có thể được sử dụng làm tài sản bảo đảm không?",
        "ground_truth": "Có. TGTK (bao gồm cả lãi) được sử dụng làm tài sản bảo đảm tại VietinBank hoặc tổ chức tín dụng khác nếu được chấp thuận.",
        "reference_contexts": "Quy định TGTK tại VietinBank - Mục 2.3"
    },

    # ---- Nhóm 9: Tiền gửi trực tuyến (Online) ----
    {
        "question": "Đối tượng nào được áp dụng nhận và chi trả tiền gửi có kỳ hạn trực tuyến?",
        "ground_truth": "Áp dụng cho khách hàng tổ chức (qua VietinBank eFAST/ERP-Connect) và khách hàng cá nhân (qua VietinBank iPay).",
        "reference_contexts": "Quy định TGCKH - Mục I.4; Điều kiện điều khoản tiền gửi có kỳ hạn trực tuyến - Trang 2"
    },
    {
        "question": "Trong tiền gửi trực tuyến, phương thức 'Tự động tái tục' hoạt động như thế nào?",
        "ground_truth": "VietinBank sẽ tự động kéo dài thời hạn gửi tiền với một kỳ hạn mới bằng kỳ hạn ban đầu theo lãi suất hiện hành tại thời điểm tái tục.",
        "reference_contexts": "Điều kiện điều khoản tiền gửi có kỳ hạn trực tuyến - Mục 2.b"
    },
    {
        "question": "Khi rút tiền gửi trực tuyến trước hạn, lãi suất được tính như thế nào?",
        "ground_truth": "Phần tiền rút trước hạn áp dụng mức lãi suất tiền gửi không kỳ hạn thấp nhất của VietinBank tại thời điểm rút. Phần tiền gửi còn lại (nếu có) vẫn được áp dụng mức lãi suất đang áp dụng cho khoản tiền gửi đó.",
        "reference_contexts": "Điều kiện điều khoản tiền gửi có kỳ hạn trực tuyến - Mục 3"
    },

    # ---- Nhóm 10: Phương pháp tính lãi ----
    {
        "question": "Công thức tính lãi ngày cho tài khoản thanh toán tại VietinBank là gì?",
        "ground_truth": "Số tiền lãi ngày = (Số dư thực tế x Lãi suất tính lãi) / 365.",
        "reference_contexts": "Phương pháp tính lãi tài khoản thanh toán - Mục 3"
    },
    {
        "question": "Thời hạn tính lãi của tài khoản thanh toán được xác định từ lúc nào?",
        "ground_truth": "Xác định từ ngày TKTT được ghi Có đến ngày liền kề trước ngày khách hàng rút tiền (tính ngày đầu, bỏ ngày cuối).",
        "reference_contexts": "Phương pháp tính lãi tài khoản thanh toán - Mục 2"
    },
    {
        "question": "Cơ sở để xác định số dư tính lãi hàng ngày là gì?",
        "ground_truth": "Là số dư thực tế trên TKTT tại thời điểm cuối mỗi ngày trong thời hạn tính lãi.",
        "reference_contexts": "Phương pháp tính lãi tài khoản thanh toán - Mục 3"
    },

    # ---- Nhóm 11: Hồ sơ & Thủ tục mở tài khoản (TKTT) ----
    {
        "question": "Để mở TKTT, công dân Việt Nam cần cung cấp giấy tờ tùy thân gì?",
        "ground_truth": "Thẻ Căn cước công dân hoặc Thẻ căn cước hoặc Căn cước điện tử (VNeID).",
        "reference_contexts": "Quy định hồ sơ, trình tự, thủ tục mở TKTT - Mục 1.1"
    },
    {
        "question": "Người dưới 14 tuổi chưa có Thẻ căn cước cần giấy tờ gì để mở tài khoản qua người giám hộ?",
        "ground_truth": "Cần Giấy khai sinh của người dưới 14 tuổi kèm theo giấy tờ tùy thân và giấy tờ chứng minh tư cách đại diện của người giám hộ.",
        "reference_contexts": "Quy định hồ sơ, trình tự, thủ tục mở TKTT - Mục 1.2"
    },
    {
        "question": "Thủ tục đối chiếu sinh trắc học đối với chủ tài khoản cá nhân diễn ra như thế nào?",
        "ground_truth": "VietinBank gặp mặt trực tiếp chủ tài khoản để kiểm tra giấy tờ tùy thân và đối chiếu khớp đúng thông tin sinh trắc học của khách hàng theo quy định.",
        "reference_contexts": "Quy định hồ sơ, trình tự, thủ tục mở TKTT - Mục 2.2.1"
    },
    {
        "question": "Trường hợp chủ tài khoản là người nước ngoài không có mặt tại Việt Nam thì VietinBank xác minh thông tin như thế nào?",
        "ground_truth": "VietinBank thực hiện xác minh thông tin nhận biết khách hàng thông qua bên thứ ba hoặc thông qua việc thuê tổ chức khác.",
        "reference_contexts": "Quy định hồ sơ, trình tự, thủ tục mở TKTT - Mục 2.2.1"
    },

    # ---- Nhóm 12: Xử lý tra soát, khiếu nại ----
    {
        "question": "Thời hạn tối thiểu khách hàng được quyền đề nghị tra soát kể từ ngày phát sinh giao dịch là bao nhiêu lâu?",
        "ground_truth": "Thời hạn đề nghị tra soát, khiếu nại không ít hơn 60 ngày kể từ ngày phát sinh giao dịch yêu cầu tra soát.",
        "reference_contexts": "Quy định hồ sơ, trình tự, thủ tục mở TKTT - Mục 3.1"
    },
    {
        "question": "VietinBank có tối đa bao nhiêu ngày để trả lời khiếu nại của khách hàng?",
        "ground_truth": "Không quá 30 ngày làm việc kể từ ngày tiếp nhận được yêu cầu khiếu nại của khách hàng.",
        "reference_contexts": "Quy định hồ sơ, trình tự, thủ tục mở TKTT - Mục 3.1"
    },
    {
        "question": "Sau khi thông báo kết quả tra soát, nếu phát sinh lỗi không do khách hàng, VietinBank bồi hoàn tổn thất trong vòng bao lâu?",
        "ground_truth": "Trong thời hạn tối đa 05 ngày làm việc kể từ ngày thông báo kết quả tra soát, khiếu nại.",
        "reference_contexts": "Quy định hồ sơ, trình tự, thủ tục mở TKTT - Mục 3.2"
    },
    {
        "question": "Nếu hết thời hạn giải quyết khiếu nại mà vẫn chưa xác định được nguyên nhân lỗi thuộc bên nào, các bên sẽ xử lý ra sao?",
        "ground_truth": "Trong vòng 15 ngày làm việc tiếp theo, VietinBank và khách hàng thỏa thuận về phương án xử lý. Nếu không thỏa thuận được thì giải quyết theo quy định pháp luật.",
        "reference_contexts": "Quy định hồ sơ, trình tự, thủ tục mở TKTT - Mục 3.2"
    },

    # ---- Nhóm 13: Bảo mật & Cảnh báo rủi ro ----
    {
        "question": "Khách hàng có được phép cho người khác mượn hoặc thuê tài khoản thanh toán của mình không?",
        "ground_truth": "Tuyệt đối không được cho thuê, mượn hoặc bán TKTT, thẻ ngân hàng; không cho mượn giấy tờ định danh để người khác mở tài khoản dưới danh nghĩa mình.",
        "reference_contexts": "Thông báo nội dung cần lưu ý khi mở, sử dụng TKTT"
    },
    {
        "question": "VietinBank khuyến cáo khách hàng làm gì khi nghi ngờ tài khoản bị lợi dụng hoặc chiếm đoạt tiền?",
        "ground_truth": "Thông báo ngay cho VietinBank qua các điểm giao dịch hoặc gọi Tổng đài 1900 558 868 để được hỗ trợ kịp thời.",
        "reference_contexts": "Thông báo nội dung cần lưu ý khi mở, sử dụng TKTT"
    },

    # ---- Nhóm 14: Xử lý sự cố thẻ/hợp đồng tiết kiệm ----
    {
        "question": "Nếu thẻ tiết kiệm bị mất, sau bao nhiêu ngày kể từ khi được cấp thẻ mới khách hàng mới được quyền rút tiền?",
        "ground_truth": "Sau 5 ngày kể từ ngày cấp thẻ tiết kiệm mới, nếu không có tranh chấp hay khiếu nại, khách hàng có quyền rút tiền.",
        "reference_contexts": "Quy định TGTK tại VietinBank - Mục 5.1"
    },
    {
        "question": "Trường hợp hợp đồng tiền gửi có kỳ hạn bị mất hoặc rách, việc chi trả được căn cứ vào đâu?",
        "ground_truth": "Việc chi trả sẽ được thực hiện theo bản Hợp đồng tiền gửi do VietinBank giữ.",
        "reference_contexts": "Quy định TGCKH - Mục III"
    },
    {
        "question": "Số điện thoại tổng đài hỗ trợ khách hàng của VietinBank là số nào?",
        "ground_truth": "Số tổng đài là 1900 558 868.",
        "reference_contexts": "Thông báo nội dung cần lưu ý khi mở, sử dụng TKTT; FAQ trang 3"
    },

    # ---- Nhóm 15: Câu hỏi kiểm tra tính logic (Tricky/Out-of-scope) ----
    {
        "question": "Tôi có thể yêu cầu VietinBank cấp bản sao y hợp đồng tiền gửi nếu bản gốc bị nhàu nát không?",
        "ground_truth": "Có. Khách hàng có thể đề nghị VietinBank cung cấp bản sao y Hợp đồng tiền gửi tại chi nhánh ký kết hợp đồng.",
        "reference_contexts": "Quy định TGCKH - Mục III; Mục 4.1"
    }
]
