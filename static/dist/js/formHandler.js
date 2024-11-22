const dropArea = document.getElementById("dropArea");
const uploadInput = document.getElementById("upload");
const preview = document.getElementById("preview");
const form = document.getElementById("myForm");
const label = document.getElementById("uploadLabel");
const tips = document.getElementById("tips");

// Handle drag-and-drop events
dropArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropArea.classList.add("bg-orange-200"); // Highlight area
});

dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("bg-orange-200");
});

dropArea.addEventListener("drop", (e) => {
  e.preventDefault();
  dropArea.classList.add("hidden");
  
  const files = e.dataTransfer.files;
  if (files.length) {
    const file = files[0];
    uploadInput.files = e.dataTransfer.files; // Update input element
    previewAndSubmit(file); // Preview and auto-submit
  }
});

// Preview image and auto-submit
function previewAndSubmit(file) {
  const reader = new FileReader();
  reader.onload = (e) => {
    const imageData = e.target.result;
    preview.src = imageData;
    
    // Simpan URL ke localStorage
    localStorage.setItem('previewImage', imageData);

    form.submit(); // Auto-submit the form
  };
  reader.readAsDataURL(file);
}

// Handle file upload via input
uploadInput.addEventListener("change", (event) => {
  const file = event.target.files[0];
  if (file) {
    previewAndSubmit(file);
  }
});

// Menampilkan gambar dari localStorage jika ada
window.addEventListener('load', function () {
  const previewURL = localStorage.getItem('previewImage');
  if (previewURL) {
    preview.src = previewURL;
    preview.classList.remove('hidden');
    dropArea.classList.add("bg-transparent");
    dropArea.classList.remove("border-2" , "border-dotted", "border-primary");
    label.classList.add("text-transparent");
    tips.classList.remove("hidden");
  }
});
