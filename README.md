Name : Andrew Wanarahardja
NPM : 2406407373
Class : PBP A

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Membuat direktori baru, mengaktifkan virtual environment
    Menambah berkas seperti .env, .env.prod, .gitignore, requirements.txt
    menginstall requiremnets dari requirements.txt
    migrate
    start project django

    python manage.py startapp main

    pada views.py membuat model dengan melakukan assignment field tertentu terhadap suatu       
        variable sesuai spesifikasi yang diminta tugas

    membuat sebuah fungsi yang mengembalikan nilai nama toko, nama, npm, dan kelas. digunakan untuk 
        mengubah nilai yang ditampilkan di main.html

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    Bagan :
    url request --> url.py --> views.py --> template.py --> output
                                 |  ^  
                                 v  |
                               models.py
                                 |  ^  
                                 v  |
                               database

    Penjelasan : 
    ketika seorang user mengetik url, masuk ke urls.py yang memastikan url yang ditulis benar. Jika 
        benar, lanjut ke views.py. views.py mengirim querysets ke models.py dan models.py berinteraksi dengan database untuk mengembalikan resultset ke views.py. informasi yang didapat lalu ditampilkan berdasarkan format dalam main.html dalam direktori templates.

3. Jelaskan peran settings.py dalam proyek Django!
    Fungsi settings.py adalah menentukan database, menentukan siapa yang bisa melakukan launch server, 
        men-enable dan disable mode debugging, mencatat app apa saja yang ada dalam project.

4. Bagaimana cara kerja migrasi database di Django?
    mengubah databse berdasarkan perubahan yang dibuat pada models.py
    python manage.py makemigrations : membuat file pada migrations yang mendeskripsikan perubahan
                                      yang akan dilakukan
    python manage.py migrations : mengubah database berdasarkan perubahan pada models.py

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Karena django berdasarkan python yang relatif mudah untuk digunakan, mengikuti struktur MVT


6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    No interaction = no feedback, cuz it was online