document.addEventListener('DOMContentLoaded', function() {
    const tabs = document.querySelectorAll('.auth-tabs a');
    tabs.forEach(tab => {
      tab.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector('.auth-tabs a.active').classList.remove('active');
        document.querySelector('.auth-pane.active').classList.remove('active');
        this.classList.add('active');
        document.querySelector(this.getAttribute('href')).classList.add('active');
      });
    });
  });