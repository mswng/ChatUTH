function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    const chatMessages = document.getElementById("chatMessages");

    if (message !== "") {
        const userMsg = document.createElement("div");
        userMsg.className = "message user";
        userMsg.textContent = message;
        chatMessages.appendChild(userMsg);
        input.value = "";

        setTimeout(() => {
            const botMsg = document.createElement("div");
            botMsg.className = "message bot";
            botMsg.textContent = "Đây là phản hồi tự động.";
            chatMessages.appendChild(botMsg);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }, 600);
    }
}

let chatCount = 2; // Giả sử có sẵn 2 đoạn chat

function addChat() {
    const chatList = document.getElementById("chatList");

    // Tạo phần tử chính cho đoạn chat
    const chatItem = document.createElement("div");
    chatItem.className = "chat-item";

    // Tạo tên đoạn chat
    const chatName = document.createElement("span");
    chatName.className = "chat-name";
    chatName.textContent = "Cuộc trò chuyện " + chatCount;
    chatItem.appendChild(chatName);

    // Tạo phần tuỳ chọn (⋮)
    const chatOptions = document.createElement("div");
    chatOptions.className = "chat-options";

    const menuButton = document.createElement("button");
    menuButton.className = "menu-button";
    menuButton.textContent = "⋮";
    menuButton.onclick = function () {
        toggleMenu(menuButton);
    };

    const dropdownMenu = document.createElement("div");
    dropdownMenu.className = "dropdown-menu";

    const deleteOption = document.createElement("div");
    deleteOption.textContent = "🗑️ Xóa";
    deleteOption.onclick = function () {
        chatItem.remove();
    };

    dropdownMenu.appendChild(deleteOption);
    chatOptions.appendChild(menuButton);
    chatOptions.appendChild(dropdownMenu);
    chatItem.appendChild(chatOptions);

    // Thêm đoạn chat mới vào danh sách
    chatList.appendChild(chatItem);
    chatCount++;
}


function selectChat(name) {
    document.getElementById("chatTitle").textContent = name;
    document.getElementById("chatMessages").innerHTML = ""; // Reset chat
}

document.getElementById("searchChat").addEventListener("input", function () {
    const query = this.value.toLowerCase();
    const items = document.querySelectorAll(".chat-item");
    items.forEach(item => {
        item.style.display = item.textContent.toLowerCase().includes(query) ? "block" : "none";
    });
});

function handleCredentialResponse(response) {
    console.log("Người dùng đã đăng nhập:", response);
    alert("Đăng nhập thành công bằng Gmail!");
}

function toggleMenu(button) {
    const menu = button.nextElementSibling;
    const allMenus = document.querySelectorAll(".dropdown-menu");
    allMenus.forEach(m => {
        if (m !== menu) m.style.display = "none"; // Ẩn các menu khác
    });
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}

function deleteThisChat(deleteButton) {
    const chatItem = deleteButton.closest(".chat-item");
    chatItem.remove();
}

function logout() {

}

function openIframe(url) {
    document.getElementById('iframePopup').src = url;
    document.getElementById('iframeOverlay').style.display = 'flex';
}

function closeIframe() {
    document.getElementById('iframePopup').src = '';
    document.getElementById('iframeOverlay').style.display = 'none';
}
