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

**Các biến thể tiêu biểu:**
- **Double Exponential Smoothing (DES):** Được thiết kế cho các chuỗi thời gian không dừng (non-stationary), bổ sung thêm một tham số để làm phẳng xu hướng (trend) của dữ liệu.

- **Triple Exponential Smoothing (TES):** Tương tự DES nhưng có thêm khả năng xử lý tính mùa vụ (seasonality) thông qua một tham số thứ ba.

### Các phương pháp dựa trên dự báo khác (Other Forecasting-based Methods)

Về cơ bản, bất kỳ mô hình hồi quy nào có khả năng dự đoán giá trị tương lai từ dữ liệu lịch sử đều có thể được sử dụng làm lõi dự báo. Một số kiến trúc cụ thể khác được ứng dụng bao gồm:
- **OceanWNN:** Sử dụng Mạng nơ-ron Wavelet (Wavelet-Neural Networks).

- **NoveltySVR:** Sử dụng các kỹ thuật hồi quy cổ điển, cụ thể là thuật toán Máy vectơ hỗ trợ (Support Vector Machine - SVM) đóng vai trò làm đơn vị dự báo lõi.

![Tổng quan về các phương pháp autoencoder để phát hiện bất thường trong chuỗi thời gian](hinh%202.png)

### Phương pháp Dựa trên Tái thiết (Reconstruction-based Methods)
Phương pháp tái thiết đại diện cho hành vi bình thường bằng cách mã hóa các chuỗi con (sub-sequences) của một chuỗi thời gian huấn luyện bình thường vào một không gian chiều thấp (low-dimensional space). Sau đó, các chuỗi con này được tái thiết (giải mã) từ không gian chiều thấp đó và được đem ra so sánh trực tiếp với các chuỗi con nguyên bản ban đầu. Sự khác biệt giữa chuỗi tái thiết và chuỗi ban đầu (còn gọi là sai số tái thiết) được sử dụng để phát hiện các điểm bất thường. Nhìn chung, dữ liệu đầu vào cho quá trình tái thiết này là các chuỗi con từ tập dữ liệu huấn luyện (training sub-sequences).

### Bộ mã hóa tự động (Autoencoder)

**Nguyên lý hoạt động:**
Autoencoder là một dạng mạng nơ-ron nhân tạo được thiết kế để học cách tái tạo lại tập dữ liệu đầu vào thông qua một kích thước mã hóa (encoding) nhỏ hơn kích thước ban đầu, nhằm tránh việc mạng chỉ đơn thuần học cách sao chép y hệt dữ liệu (identity reconstruction). Là một ý tưởng cốt lõi, autoencoder sẽ cố gắng học được biểu diễn tiềm ẩn (latent representation) tốt nhất thông qua một hàm mất mát tái thiết (reconstruction loss). Do đó, nó sẽ học cách nén tập dữ liệu thành một đoạn mã ngắn, sau đó giải nén đoạn mã này thành một tập dữ liệu khớp nhất có thể so với bản gốc ban đầu.

Về mặt hình thức, với hai hàm chuyển đổi $E$ và $D$, lần lượt được gọi là bộ mã hóa (encoder) và bộ giải mã (decoder), nhiệm vụ của một bộ tự mã hóa (autoencoder) là như sau:
$$
\begin{aligned}
\phi &: \mathbb{T}_\ell \rightarrow \mathbb{Z} \\
\psi &: \mathbb{Z} \rightarrow \mathbb{T}_\ell \\
\phi, \psi &= \arg \min_{\phi, \psi} \mathcal{L}(T_{i,\ell}, \psi(\phi(T_{i,\ell})))
\end{aligned}
$$
Trong đó, $\mathcal{L}$ là hàm mất mát, thường được định nghĩa là sai số toàn phương trung bình (Mean Squared Error - MSE) giữa đầu vào và bản tái thiết của nó:

$$
\|X - \psi(\phi(T_{i,\ell}))\|^2
$$

Hàm mất mát này đặc biệt phù hợp cho bài toán xử lý các chuỗi con trong chuỗi thời gian, do nó tương ứng trực tiếp với khoảng cách Euclid giữa tín hiệu gốc và tín hiệu tái thiết.

Sai số tái thiết đóng vai trò như một **điểm số bất thường (anomaly score)** trong bài toán phát hiện dị thường. Do mô hình Autoencoder chỉ được huấn luyện trên các chuỗi con bình thường (không chứa dị thường), nó được tối ưu hóa để tái thiết tốt các mẫu dữ liệu "khỏe mạnh". Vì vậy, các chuỗi con có đặc trưng khác biệt so với phân phối huấn luyện sẽ dẫn đến sai số tái thiết lớn hơn.

![Tổng quan về các phương pháp GAN để phát hiện bất thường trong chuỗi thời gian](hinh-4.png)

*Hình: Tổng quan về các phương pháp GAN để phát hiện bất thường trong chuỗi thời gian*

---

**Các biến thể / Khung ứng dụng tiêu biểu:**

- **EncDec-AD:** Là một trong những mô hình đầu tiên áp dụng kiến trúc encoder–decoder kết hợp sai số tái thiết để đánh giá mức độ bất thường.

- **LSTM-VAE và MSCRED:** Tích hợp các cơ chế ghi nhớ như LSTM và Convolutional LSTM vào kiến trúc autoencoder nhằm khai thác tốt hơn thông tin chuỗi thời gian.

- **OmniAnomaly:** Phương pháp dựa trên autoencoder sử dụng mạng GRU kết hợp với kỹ thuật *planar normalizing flow* để mô hình hóa phân phối phức tạp của dữ liệu.

- **STORN và DONUT:** Hai phương pháp này sử dụng Variational Autoencoder (VAE) cho phát hiện dị thường. Đặc biệt, DONUT bổ sung bước tiền xử lý để xử lý dữ liệu thiếu thông qua phương pháp MCMC.

- **BAGEL:** Phiên bản cải tiến của DONUT, sử dụng kiến trúc *conditional VAE* thay vì VAE truyền thống.

- **VELC:** Áp dụng các ràng buộc bổ sung lên VAE, trong đó bộ giải mã (decoder) được điều chuẩn dựa trên các mẫu bất thường có sẵn nhằm hạn chế khả năng tái thiết tốt cả dữ liệu dị thường.

- **CAE (Convolutional Autoencoder):** Sử dụng mạng tích chập để ánh xạ chuỗi thời gian sang không gian biểu diễn dạng ảnh. Đồng thời, thuật toán tận dụng SAX (Symbolic Aggregate approXimation) để tăng tốc tìm kiếm thông qua biểu diễn nhúng.

- **DeepNAP:** Mô hình autoencoder dạng sequence-to-sequence với khả năng *pre-detection*, cho phép phát hiện bất thường trước khi chúng thực sự xảy ra.

### Mạng đối nghịch sinh (Generative Adversarial Networks  - GAN)
**Nguyên lý hoạt động:**
Mạng đối nghịch sinh (GAN) ban đầu được đề xuất riêng cho mục đích tạo ảnh, nhưng kiến trúc này cũng hoàn toàn có thể được dùng để tạo ra các chuỗi dữ liệu thời gian. GAN bao gồm hai thành phần thiết yếu: (i) Một bộ phận dùng để sinh/tạo ra chuỗi thời gian mới, và (ii) một bộ phận dùng để phân biệt chuỗi thời gian đang có. Cả hai thành phần này đều đóng vai trò then chốt để phát hiện bất thường.

Cụ thể hơn, mạng GAN gồm hai mạng nơ-ron hoạt động cạnh tranh. Đầu tiên là Generator (Bộ sinh) $G(z,\theta_{g})$ với $\theta_{g}$ là các tham số của nó. Mạng thứ hai là Discriminator (Bộ phân biệt) $D(x,\theta_{d})$ với $\theta_{d}$ là các tham số tương ứng. Đầu ra của Discriminator là một giá trị vô hướng (scalar) đại diện cho xác suất chứng minh mẫu dữ liệu đầu vào thực sự đến từ tập dữ liệu gốc. Việc huấn luyện hai mạng này được coi là một bài toán tối ưu hóa hai người chơi (two-player optimization): Mạng Discriminator cố gắng tối đa hóa độ chính xác của nó, trong khi Generator thì cố gắng giảm thiểu độ chính xác của Discriminator bằng cách tạo ra dữ liệu giả mạo giống hệt đồ thật.

Đối với mục đích tìm kiếm bất thường, Generator sẽ được huấn luyện để chỉ sinh ra các chuỗi con được dán nhãn là "bình thường", và Discriminator được huấn luyện để phân định rạch ròi giữa dữ liệu thật (bình thường) và dữ liệu giả (bất thường). Do đó, ta có thể dùng song song cả Discriminator và Generator để tìm ra điểm bất thường:
- Đầu tiên, do Discriminator được huấn luyện để phân biệt giữa dữ liệu thật và dữ liệu giả, nên bản thân nó có thể được sử dụng trực tiếp như một công cụ phát hiện bất thường.

- Tuy nhiên, Generator cũng đóng vai trò quan trọng không kém. Vì được huấn luyện để sinh ra các chuỗi con mang đặc trưng "bình thường", nó sẽ gặp khó khăn (tạo ra sai số lớn) khi cố gắng tái tạo các chuỗi có đặc tính bất thường. Do đó, khoảng cách Euclid giữa chuỗi con cần đánh giá và chuỗi được sinh bởi Generator là một chỉ số quan trọng để xác định mức độ bất thường.
**Các biến thể / Khung ứng dụng tiêu biểu:**

- **MAD-GAN, USAD và TAnoGAN:** Đây là nhóm các phương pháp đề xuất huấn luyện kiến trúc GAN trên các phân đoạn bình thường của chuỗi thời gian. Điểm số bất thường (anomaly score) được xác định dựa trên sự kết hợp giữa tổn thất của Discriminator (discriminator loss) và tổn thất tái thiết (reconstruction loss).

- **VAE-GAN:** Mô hình này kết hợp ưu điểm của GAN và Variational Autoencoder (VAE). Trong đó, Generator được thiết kế như một VAE và cạnh tranh trực tiếp với Discriminator. Điểm số bất thường cũng được tính toán theo cơ chế tương tự như trong MAD-GAN và USAD.

## Kết luận (Conclusions)
Trong bài khảo sát này, chúng tôi đã xem xét toàn diện bài toán phát hiện bất thường trong chuỗi thời gian. Bài viết bắt đầu bằng việc xây dựng một hệ thống phân loại (taxonomy) chi tiết về các loại chuỗi thời gian, các dạng bất thường và các phương pháp phát hiện. Các phương pháp này được phân nhóm theo lăng kính quy trình (process-centric categories). Từ đó, chúng tôi mô tả chi tiết các thuật toán phổ biến nhất trong từng nhóm và cung cấp một danh sách mở rộng các phương pháp hiện có. Cuối cùng, bài viết thảo luận chuyên sâu về vấn đề đánh giá hiệu năng (benchmarking), liệt kê các tập dữ liệu chuẩn, các thước đo truyền thống cùng với hạn chế của chúng, cũng như những nỗ lực gần đây nhằm điều chỉnh các thước đo này cho phù hợp với đặc thù của chuỗi thời gian.
### Thách thức hiện tại
Dù đã trải qua nhiều thập kỷ nghiên cứu, phát hiện bất thường trong chuỗi thời gian vẫn là một bài toán đầy thách thức. Trong lịch sử, các cộng đồng nghiên cứu thường tiếp cận vấn đề một cách rời rạc và phát triển các phương pháp dựa trên nền tảng lý thuyết riêng biệt. Sự thiếu thống nhất trong việc sử dụng chung các thước đo và tập dữ liệu đánh giá đã khiến việc đo lường tiến bộ thực tế trở nên khó khăn. Tuy nhiên, những nỗ lực xây dựng các bộ dữ liệu chuẩn (benchmarks) gần đây \cite{113, 185} đã đóng góp tích cực vào việc đánh giá sự phát triển và lựa chọn phương pháp phù hợp cho các bài toán cụ thể.

### Định hướng nghiên cứu tương lai
Mặc dù đã đạt được nhiều tiến bộ đáng kể, lĩnh vực này vẫn mở ra nhiều hướng nghiên cứu tiềm năng trong tương lai:

- **Thống nhất bộ dữ liệu chuẩn (Benchmarking):** Hiện vẫn chưa có sự đồng thuận về một bộ benchmark chung cho toàn bộ cộng đồng. Các bộ dữ liệu hiện có còn tồn tại nhiều hạn chế về tính đa dạng của chuỗi thời gian, loại hình bất thường cũng như độ tin cậy của nhãn. Do đó, việc xây dựng một hệ thống đánh giá chuẩn hóa và toàn diện hơn là rất cần thiết.

- **Lựa chọn mô hình và Học máy tự động (AutoML):** Với sự xuất hiện của nhiều phương pháp mới mỗi năm, các nghiên cứu gần đây cho thấy **không tồn tại một mô hình duy nhất tối ưu cho mọi tập dữ liệu**. Điều này thúc đẩy các hướng tiếp cận như kết hợp mô hình (ensembling), lựa chọn mô hình và AutoML. Một số thực nghiệm cho thấy việc sử dụng các mô hình phân loại chuỗi thời gian cơ bản để hỗ trợ lựa chọn mô hình phát hiện bất thường có thể cải thiện đáng kể độ chính xác, thậm chí lên tới gấp đôi trong một số trường hợp.

- **Mở rộng sang các dạng dữ liệu phức tạp:** Phần lớn các phương pháp không giám sát hiện nay chủ yếu tập trung vào chuỗi thời gian đơn biến (univariate), trong khi các bài toán thực tế thường phức tạp hơn. Các nghiên cứu trong tương lai cần hướng đến các kịch bản như: chuỗi đa biến (multivariate), dữ liệu dòng thời gian thực (streaming), dữ liệu bị thiếu (missing values), nhãn thời gian không liên tục, dữ liệu không đồng nhất (heterogeneous), hoặc sự kết hợp của các yếu tố này. Việc phát triển các phương pháp mạnh mẽ và chính xác cho các trường hợp này là một yêu cầu cấp thiết.