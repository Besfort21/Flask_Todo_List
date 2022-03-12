window.onload = function(){
    document.getElementById("download").addEventListener("click",()=>{
        const svpdf = this.document.getElementById("save_as_pdf");
        var opt = {
            margin: 1,
            filename: 'myfile.pdf',
            image: { type: 'jpeg', quality: 0.98 },
            html2canvas: { scale: 2 },
            jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
        };
        html2pdf().from(svpdf).set(opt).save();

    })
}