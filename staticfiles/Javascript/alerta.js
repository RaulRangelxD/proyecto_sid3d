function confirmDelete() {
    var result = confirm("Are you sure you want to delete this product?");
    if (result) {
        // If user confirms, proceed with the deletion
        // You can redirect to the delete endpoint here
        window.location.href = "/tasks/"; // Redirect to delete endpoint
    }
}