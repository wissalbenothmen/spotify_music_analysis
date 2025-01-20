document.addEventListener('DOMContentLoaded', function() {
    const tableContainer = document.getElementById('table-container');
    const table = tableContainer.querySelector('table');
    const tbody = table.querySelector('tbody');
    const thead = table.querySelector('thead');
    const prevPage = document.getElementById('prev-page');
    const nextPage = document.getElementById('next-page');
    let data = [];
    let currentPage = 1;
    const rowsPerPage = 10;

    fetch('/static/data/spotify_tracks.csv')
        .then(response => response.text())
        .then(csvData => {
            parseCSV(csvData);
        })
        .catch(error => console.error('Error loading the CSV file:', error));

    function parseCSV(csvData) {
        const lines = csvData.split('\n');
        const headers = lines[0].split(',');
        data = lines.slice(1).map(line => {
            const values = line.split(',');
            const row = {};
            headers.forEach((header, index) => {
                row[header.trim()] = values[index].trim();
            });
            return row;
        });
        renderTable(headers, data.slice(0, rowsPerPage));
        updatePagination();
    }

    function renderTable(headers, rows) {
        thead.innerHTML = '<tr></tr>';
        headers.forEach(header => {
            const th = document.createElement('th');
            th.textContent = header;
            thead.querySelector('tr').appendChild(th);
        });

        tbody.innerHTML = '';
        rows.forEach(row => {
            const tr = document.createElement('tr');
            headers.forEach(header => {
                const td = document.createElement('td');
                td.textContent = row[header];
                tr.appendChild(td);
            });
            tbody.appendChild(tr);
        });
    }

    function updatePagination() {
        const totalPages = Math.ceil(data.length / rowsPerPage);
        const pagination = tableContainer.querySelector('.pagination');
        pagination.innerHTML = '';

        const prevLi = document.createElement('li');
        prevLi.className = 'page-item';
        if (currentPage === 1) {
            prevLi.classList.add('disabled');
        }
        const prevLink = document.createElement('a');
        prevLink.className = 'page-link';
        prevLink.href = '#';
        prevLink.textContent = 'Previous';
        prevLink.addEventListener('click', function(event) {
            event.preventDefault();
            if (currentPage > 1) {
                currentPage--;
                renderTable(Array.from(thead.querySelector('tr').children).map(th => th.textContent), data.slice((currentPage - 1) * rowsPerPage, currentPage * rowsPerPage));
                updatePagination();
            }
        });
        prevLi.appendChild(prevLink);
        pagination.appendChild(prevLi);

        for (let i = 1; i <= totalPages; i++) {
            const li = document.createElement('li');
            li.className = 'page-item';
            if (i === currentPage) {
                li.classList.add('active');
            }
            const link = document.createElement('a');
            link.className = 'page-link';
            link.href = '#';
            link.textContent = i;
            link.addEventListener('click', function(event) {
                event.preventDefault();
                currentPage = i;
                renderTable(Array.from(thead.querySelector('tr').children).map(th => th.textContent), data.slice((currentPage - 1) * rowsPerPage, currentPage * rowsPerPage));
                updatePagination();
            });
            li.appendChild(link);
            pagination.appendChild(li);
        }

        const nextLi = document.createElement('li');
        nextLi.className = 'page-item';
        if (currentPage === totalPages) {
            nextLi.classList.add('disabled');
        }
        const nextLink = document.createElement('a');
        nextLink.className = 'page-link';
        nextLink.href = '#';
        nextLink.textContent = 'Next';
        nextLink.addEventListener('click', function(event) {
            event.preventDefault();
            if (currentPage < totalPages) {
                currentPage++;
                renderTable(Array.from(thead.querySelector('tr').children).map(th => th.textContent), data.slice((currentPage - 1) * rowsPerPage, currentPage * rowsPerPage));
                updatePagination();
            }
        });
        nextLi.appendChild(nextLink);
        pagination.appendChild(nextLi);
    }
});
