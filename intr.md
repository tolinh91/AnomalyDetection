# Title Here

## Khái niệm và phân loại điểm bất thường

## Các phương pháp dựa trên dự đoán (Prediction-based Methods)
Các phương pháp dựa trên dự đoán nhằm mục đích phát hiện các bất thường bằng cách dự đoán các hành vi bình thường dự kiến dựa trên một tập huấn luyện gồm các chuỗi thời gian hoặc chuỗi con (có chứa bất thường hoặc không). Ví dụ, hãy tưởng tượng bạn đang theo dõi biểu đồ giá của các mã cổ phiếu như PNJ hay FPT..., những biến động chệch hướng hoàn toàn so với xu hướng chung chính là những 'tín hiệu' mà chúng ta cần bắt được.

Để giải quyết bài toán này, phương pháp dựa trên dự đoán là một trong những hướng tiếp cận mạnh mẽ nhất. Có hai loại cấp độ của phương pháp này là dựa trên dự báo và dựa trên tái thiết. Chúng tôi đã liệt kê tất cả các phương pháp đã đề cập trong Bảng 3 dưới đây.

![Bảng 3. Tóm tắt các phương pháp phát hiện bất thường dựa trên dự đoán.](source\Hinh3)

### Phương pháp dựa trên dự báo (Forecasting-based Methods)
Các phương pháp dựa trên dự báo hoạt động dựa trên một nguyên tắc cốt lõi: sử dụng các điểm hoặc chuỗi dữ liệu trong quá khứ để huấn luyện một mô hình dự đoán giá trị tiếp theo. Kết quả dự báo này gắn liền trực tiếp với các quan sát trước đó trong chuỗi thời gian. Các điểm dữ liệu sau đó sẽ được so sánh với giá trị gốc; độ lệch (sai số dự báo) càng lớn thì khả năng điểm đó là bất thường càng cao.

### Exponential Smoothing (Làm phẳng số mũ)
**Nguyên lý hoạt động:** Exponential Smoothing là một trong những kỹ thuật dự báo sớm nhất được đề xuất trong tài liệu học thuật. Đây là một phương pháp làm phẳng phi tuyến, dự đoán các điểm dữ liệu bằng cách sử dụng dữ liệu quá khứ và gán các trọng số giảm dần theo cấp số nhân cho các quan sát cũ hơn. 

Về mặt toán học, giá trị ước lượng tại thời điểm hiện tại là sự kết hợp tuyến tính của các điểm dữ liệu trước đó. Tham số $\alpha \in [0,1]$ là hệ số làm mượt (smoothing factor); $\alpha$ càng nhỏ thì các điểm dữ liệu trong quá khứ càng xa vẫn có ảnh hưởng lớn hơn đến giá trị dự đoán.

Giá trị dự đoán tại thời điểm $i$, ký hiệu là $\hat{T}_i$, được xác định như sau:

$$
\hat{T}_i = (1-\alpha)^{N-1}T_{i-N} + \sum_{j=1}^{N-1}\alpha(1-\alpha)^{j-1}T_{i-j}, \quad \alpha \in [0,1]
$$
