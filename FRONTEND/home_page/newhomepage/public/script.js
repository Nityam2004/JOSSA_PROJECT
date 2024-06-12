document.addEventListener("DOMContentLoaded", () => {
    const newsList = document.getElementById("news-list");

    // Sample news data (you can add more)
    const newsData = [
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Important Announcement", date: "2024-06-10", pdf: "pdf1.pdf" },
        { title: "Exam Schedule Update", date: "2024-06-08", pdf: "pdf2.pdf" }
    ];

    // Function to add news items to the list
    function addNewsItems() {
        newsData.forEach(news => {
            const li = document.createElement("li");
            const a = document.createElement("a");
            a.href = `/uploads/${news.pdf}`;
            a.textContent = `${news.title} - ${news.date}`;
            li.classList.add("news-item");
            li.appendChild(a);
            newsList.appendChild(li);
        });
    }

    addNewsItems();
});
