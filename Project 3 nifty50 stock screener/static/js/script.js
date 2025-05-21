// Add any custom JavaScript functionality here
document.addEventListener('DOMContentLoaded', function() {
    // Show loading spinner during screen operations
    const screenForm = document.querySelector('form[action="/screen"]');
    if (screenForm) {
        screenForm.addEventListener('submit', function() {
            const submitBtn = this.querySelector('button[type="submit"]');
            submitBtn.disabled = true;
            submitBtn.innerHTML = `
                <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                Screening Stocks...
            `;
        });
    }
    
    // Add any other interactive functionality
});