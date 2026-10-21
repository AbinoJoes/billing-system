
function filterCustomers() {
    // Get the search input
    let searchInput = document
        .getElementById("customer_id")
        .value.toLowerCase()
        .trim();

    // Get all table rows
    let table = document.getElementById("customerTable");
    let rows = table.getElementsByTagName("tbody")[0]
                    .getElementsByTagName("tr");

    // Check each row
    for (let i = 0; i < rows.length; i++) {
        let customerId = rows[i].cells[0].textContent.toLowerCase();
        let customerName = rows[i].cells[1].textContent.toLowerCase();

        // Show row if ID or name matches
        if (
            customerId.includes(searchInput) ||
            customerName.includes(searchInput)
        ) {
            rows[i].style.display = "";
        } else {
            rows[i].style.display = "none";
        }
    }
}
