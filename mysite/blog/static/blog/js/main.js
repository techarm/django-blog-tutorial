// ページ読み込み完了時に実行
document.addEventListener('DOMContentLoaded', function () {
    // 記事をクリックしたときのアニメーション
    const posts = document.querySelectorAll('.post');

    posts.forEach(post => {
        post.addEventListener('click', function () {
            // クリックアニメーション
            this.style.transform = 'scale(0.98)';
            setTimeout(() => {
                this.style.transform = '';
            }, 100);
        });
    });

    // スムーズスクロール
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // コンソールにメッセージ
    console.log('Djangoブログへようこそ！');
});