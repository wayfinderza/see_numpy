document.addEventListener("DOMContentLoaded", function () {
    // Ensure each value span has proper dataset attributes
    document.querySelectorAll("span[id^='value-']").forEach(span => {
        let index = span.id.replace("value-", "");
        
        // Get data values from inline attributes (set via Jinja template)
        let sum = span.getAttribute("data-sum") || "0";
        let average = span.getAttribute("data-average") || "0";
        let count = span.getAttribute("data-count") || "0";

        // Assign the values to dataset attributes
        span.dataset.sum = sum;
        span.dataset.average = average;
        span.dataset.count = count;
        
        // Set initial display to sum (default)
        span.textContent = sum;
    });

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
