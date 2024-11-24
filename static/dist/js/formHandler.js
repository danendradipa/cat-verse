const dropArea = document.getElementById("dropArea");
const uploadInput = document.getElementById("upload");
const form = document.getElementById("myForm");

// Highlight the drop area on drag-over
dropArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropArea.classList.add("bg-orange-200"); // Highlight area
});

// Remove highlight on drag-leave
dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("bg-orange-200");
});

// Handle file drop
dropArea.addEventListener("drop", (e) => {
  e.preventDefault();
  dropArea.classList.remove("bg-orange-200");

  const files = e.dataTransfer.files;
  if (files.length) {
    uploadInput.files = e.dataTransfer.files; // Set dropped file to input
    form.submit(); // Directly submit the form
  }
});

// Handle file selection from input
uploadInput.addEventListener("change", (event) => {
  const file = event.target.files[0];
  if (file) {
    form.submit(); // Directly submit the form
  }
});