// static/js/signup.js

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

function signupUser(event) {
    event.preventDefault();
    
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const statusDisplay = document.getElementById("signup-status");

    // 상태 메시지 초기화
    statusDisplay.textContent = '';
    statusDisplay.style.color = 'red';
    statusDisplay.classList.remove('success-message', 'error-message');

    const signupApiUrl = '/auth/signup/';

    fetch(signupApiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        credentials: 'include',
        body: JSON.stringify({
            username: username,
            email: email,
            password: password
        })
    })
    .then(response => {
        if (response.status === 201) {
            return response.json().then(data => {
                statusDisplay.textContent = data.message + " 자동 로그인 되었습니다.";
                statusDisplay.style.color = '#27AE60';
                statusDisplay.classList.add('success-message');
                
                // 1.5초 후 로그인 페이지로 이동
                setTimeout(() => {
                    window.location.href = "/auth/login.html";
                }, 1500);
            });
        }
        
        // 400 Bad Request 등 오류 처리
        return response.json().then(errorData => {
            statusDisplay.classList.add('error-message');
            
            if (errorData.username) {
                statusDisplay.textContent = `아이디 오류: ${errorData.username[0]}`;
            } else if (errorData.email) {
                statusDisplay.textContent = `이메일 오류: ${errorData.email[0]}`;
            } else if (errorData.password) {
                statusDisplay.textContent = `비밀번호 오류: ${errorData.password[0]}`;
            } else {
                statusDisplay.textContent = "회원가입 실패: 입력 데이터를 확인해주세요.";
            }
        });
    })
    .catch(error => {
        console.error('Fetch Error:', error);
        statusDisplay.textContent = '서버와 통신할 수 없습니다.';
        statusDisplay.classList.add('error-message');
    });
}