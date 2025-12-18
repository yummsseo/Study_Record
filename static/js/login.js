// 쿠키에서 특정 이름의 값을 가져오는 함수 (CSRF 토큰 추출용)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // 쿠키 이름이 일치하는지 확인
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function loginUser(event) {
    event.preventDefault(); // 폼 제출 시 페이지 새로고침 방지

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    // 쿠키에서 CSRF 토큰을 가져옵니다.
    const csrftoken = getCookie('csrftoken');

    try {
        const response = await fetch('/auth/login/', { // urls.py 경로와 맞춰주세요
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken // 헤더에 CSRF 토큰 추가
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        const data = await response.json();

        if (response.ok) {
            alert(data.message);
            window.location.href = '/'; // 로그인 성공 시 이동할 페이지
        } else {
            alert(data.error || '로그인 실패');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('서버와 통신하는 중 오류가 발생했습니다.');
    }
}