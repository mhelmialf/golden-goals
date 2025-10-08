function showToast(title, message, type = 'success') {
    const toast = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon = document.getElementById('toast-icon');

    if (!toast || !toastTitle || !toastMessage || !toastIcon) {
        console.error('Toast elements not found!');
        return;
    }

    // Konfigurasi berdasarkan tipe notifikasi
    const configurations = {
        success: {
            borderColor: 'border-green-400',
            titleColor: 'text-green-600',
            icon: '✅',
        },
        error: {
            borderColor: 'border-red-400',
            titleColor: 'text-red-600',
            icon: '❌',
        },
        warning: {
            borderColor: 'border-yellow-400',
            titleColor: 'text-yellow-600',
            icon: '⚠️',
        }
    };

    const config = configurations[type] || configurations.success;

    // Reset class sebelum menambahkan yang baru
    toast.className = 'fixed top-20 right-8 p-4 px-8 rounded-xl shadow-xl z-50 opacity-0 transition-all duration-300 translate-y-0 flex items-center gap-4 bg-white';
    toastTitle.className = 'font-bold';
    
    // Terapkan style baru
    toast.classList.add(config.borderColor);
    toastTitle.classList.add(config.titleColor);
    toastIcon.textContent = config.icon;

    // Set konten
    toastTitle.textContent = title;
    toastMessage.textContent = message;

    // Tampilkan toast
    toast.classList.remove('opacity-0');
    toast.classList.add('opacity-100');

    // Sembunyikan setelah 3 detik
    setTimeout(() => {
        toast.classList.remove('opacity-100');
        toast.classList.add('opacity-0');
    }, 3000);
}