document.addEventListener("DOMContentLoaded", function () {
    const expandButton = document.getElementById("expand-btn");
    const collapseButton = document.getElementById("collapse-btn");
    const btnLoadSample1 = document.getElementById("btnLoadSample1");
    const btnLoadSample2 = document.getElementById("btnLoadSample2");

    // Function to trigger sample loading via form submission
    function loadSample(sampleId) {
        const form = document.createElement("form");
        form.method = "GET";
        form.action = `/load_sample/${sampleId}`;
        document.body.appendChild(form);
        form.submit();
    }

    // Handler for Sample 1
    btnLoadSample1.addEventListener("click", () => {
        loadSample(1);
    });

    // Handler for Sample 2
    btnLoadSample2.addEventListener("click", () => {
        loadSample(2);
    });

    let currentLevel = 0; // Tracks the currently expanded level
    let maxLevel = getMaxLevel(); // Get the max depth from the table

    function getMaxLevel() {
        let max = 0;
        document.querySelectorAll("[data-level]").forEach(row => {
            let level = parseInt(row.getAttribute("data-level"));
            if (level > max) {
                max = level;
            }
        });
        return max;
    }

    // Function to expand the next level
    window.expandNextLevel = function () {
        const nextLevel = currentLevel + 1;
        const rowsToExpand = document.querySelectorAll(`[data-level="${nextLevel}"]`);

        if (rowsToExpand.length > 0) {
            rowsToExpand.forEach(row => row.classList.remove("d-none"));
            currentLevel = nextLevel;
            collapseButton.disabled = false;
        }

        if (currentLevel >= maxLevel) {
            expandButton.disabled = true;
        }
    };

    // Function to collapse back to the global level
    window.collapseToGlobal = function () {
        if (currentLevel > 0) {
            document.querySelectorAll(`[data-level="${currentLevel}"]`).forEach(row => row.classList.add("d-none"));
            currentLevel -= 1;
        }

        if (currentLevel === 0) {
            collapseButton.disabled = true;
        }

        expandButton.disabled = false;
    };

    // Function to update displayed table values based on selected metric
    window.updateTable = function (metric) {
        document.querySelectorAll("span[id^='value-']").forEach(span => {
            let sum = span.dataset.sum || "0";
            let average = span.dataset.average || "0";
            let count = span.dataset.count || "0";

            if (metric === 'sum') {
                span.textContent = sum;
            } else if (metric === 'average') {
                span.textContent = average;
            } else if (metric === 'count') {
                span.textContent = count;
            }
        });
    };

    // Function to expand all rows
    window.expandAll = function () {
        document.querySelectorAll("tr").forEach(row => row.classList.remove("d-none"));
        currentLevel = maxLevel;
        expandButton.disabled = true;
        collapseButton.disabled = false;
    };

    // Function to collapse all rows
    window.collapseAll = function () {
        document.querySelectorAll("[data-level]").forEach(row => row.classList.add("d-none"));
        currentLevel = 0;
        expandButton.disabled = false;
        collapseButton.disabled = true;
    };

    // Initialize Bootstrap toasts
    const toastElements = document.querySelectorAll('.toast');
    toastElements.forEach(toast => {
        new bootstrap.Toast(toast).show();
    });
});
