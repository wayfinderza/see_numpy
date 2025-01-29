document.addEventListener("DOMContentLoaded", function () {
    const expandButton = document.getElementById("expand-btn");
    const collapseButton = document.getElementById("collapse-btn");

    let currentLevel = 0; // Tracks the currently visible level

    // Function to expand the next level
    window.expandNextLevel = function () {
        const nextLevel = currentLevel + 1;
        const rowsToExpand = document.querySelectorAll(`[data-level="${nextLevel}"]`);

        // Check if there are rows for the next level
        if (rowsToExpand.length > 0) {
            rowsToExpand.forEach(row => row.classList.remove("d-none")); // Show the next level
            currentLevel = nextLevel;
            collapseButton.disabled = false; // Enable collapse button
        }

        // Check if the next level is the last and disable the Expand button if so
        const furtherLevels = document.querySelectorAll(`[data-level="${nextLevel + 1}"]`);
        if (furtherLevels.length === 0) {
            expandButton.disabled = true; // No more levels to expand
        }
    };

    // Function to collapse back to the global level
    window.collapseToGlobal = function () {
        const rowsToCollapse = document.querySelectorAll(`[data-level="${currentLevel}"]`);

        // Collapse the current level rows
        rowsToCollapse.forEach(row => row.classList.add("d-none"));

        currentLevel -= 1; // Move back to the previous level

        // Disable the Collapse button if we're back at the global level
        if (currentLevel === 0) {
            collapseButton.disabled = true;
        }

        // Re-enable the Expand button since we can expand again
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
