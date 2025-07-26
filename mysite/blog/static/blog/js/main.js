// ページ読み込み完了時に実行
document.addEventListener('DOMContentLoaded', function () {
    // 閉じるボタンを取得
    const closeButtons = document.querySelectorAll('.alert .close');

    closeButtons.forEach(button => {
        button.addEventListener('click', function () {
            // 親要素（.alert）を取得
            const alert = this.closest('.alert');

            // フェードアウトアニメーション
            alert.style.transition = 'opacity 0.3s ease';
            alert.style.opacity = '0';

            // アニメーション完了後に要素を削除
            setTimeout(() => {
                alert.remove();
            }, 300);
        });
    });

    // オプション：一定時間後に自動的にメッセージを非表示にする
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        // 5秒後に自動的にフェードアウト
        setTimeout(() => {
            if (alert && alert.parentNode) {
                alert.style.transition = 'opacity 0.5s ease';
                alert.style.opacity = '0';
                setTimeout(() => {
                    if (alert.parentNode) {
                        alert.remove();
                    }
                }, 500);
            }
        }, 5000); // 5000ミリ秒 = 5秒
    });

    // フォームの二重送信防止
    const forms = document.querySelectorAll('.post-form, .delete-form');
    forms.forEach(form => {
        form.addEventListener('submit', function (e) {
            const submitButton = form.querySelector('button[type="submit"]');
            // ボタンを無効化
            submitButton.disabled = true;
            submitButton.textContent = '処理中...';
        });
    });
});