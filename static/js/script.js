document.addEventListener("DOMContentLoaded", function () {
    // Ensure global level is always visible and collapse button is disabled initially
    const globalRow = document.querySelector(".level-global");
    const expandButton = document.getElementById("expand-btn");
    const collapseButton = document.getElementById("collapse-btn");

    let currentLevel = 0; // Tracks the currently visible level

    // Function to expand the next level
    window.expandNextLevel = function () {
        const nextLevel = currentLevel + 1;
        const rowsToExpand = document.querySelectorAll(`[data-level="${nextLevel}"]`);
        
        if (rowsToExpand.length > 0) {
            rowsToExpand.forEach(row => row.classList.remove("d-none"));
            currentLevel = nextLevel;
            collapseButton.disabled = false; // Enable collapse button
        } else {
            // Disable expand button if no further levels exist
            expandButton.disabled = true;
        }
    };

    // Function to collapse back to the global level
    window.collapseToGlobal = function () {
        const rowsToCollapse = document.querySelectorAll(`[data-level="${currentLevel}"]`);
        rowsToCollapse.forEach(row => row.classList.add("d-none"));
        
        currentLevel -= 1;

        // Disable collapse button if we're back at the global level
        if (currentLevel === 0) {
            collapseButton.disabled = true;
        }

        // Re-enable expand button since we can expand again
        expandButton.disabled = false;
    };

    // Initialize Bootstrap toasts
    const toastElements = document.querySelectorAll('.toast');
    toastElements.forEach(toast => {
        new bootstrap.Toast(toast).show();
    });
});

// Function to update displayed table values based on selected metric
function updateTable(metric) {
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
}

// Function to expand all rows
function expandAll() {
    document.querySelectorAll("tr").forEach(row => {
        row.classList.remove("d-none");
    });
}

// Function to collapse all rows
function collapseAll() {
    document.querySelectorAll("tbody tr").forEach(row => {
        row.classList.add("d-none");
    });
}
