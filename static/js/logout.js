// static/js/logout.js

// CSRF 토큰 가져오기
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// 로그아웃 처리 함수
async function logoutUser(event) {
    if (event) {
        event.preventDefault();
    }
    
    const logoutUrl = '/auth/logout/';
    const token = getCookie('csrftoken');

    if (!token) {
        alert("로그아웃 실패: CSRF 토큰을 찾을 수 없습니다.");
        return;
    }

    try {
        const response = await fetch(logoutUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': token
            },
            credentials: 'include'
        });

        if (response.ok) {
            const data = await response.json();
            alert(data.message || '로그아웃 성공!');
            window.location.href = '/auth/login.html';
        } else {
            const errorData = await response.json();
            alert(`로그아웃 실패: ${errorData.detail || errorData.message || '알 수 없는 오류'}`);
        }
    } catch (error) {
        console.error("로그아웃 오류:", error);
        alert("서버 연결에 실패했습니다.");
    }
}

// 전역에서 접근 가능하도록 설정
window.logoutUser = logoutUser;