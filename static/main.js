
function totalCost(e) {
    // let c= document.getElementsByName('amount')
    let formData = new FormData(e.target)
    var form_values = Object.fromEntries(formData)
    console.log(form_values)

}