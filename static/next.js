

// const postsBox = document.getElementById('posts-box') 
// const spinnerBox = document.getElementById('spinner-box') 
// const loadBtn = document.getElementById('load-btn') 
// const loadBox = document.getElementById('loading-box')
// let visible = 3

// const handleGetData = ()=>{
//     $.ajax({
//         type: 'GET',
//         url: `/posts-json/${visible}/`,
//         success: function(response){
//             // console.log(response.max)
//             max_size = response.max
//             const data = response.data
//             spinnerBox.classList.remove('not-visible')
//             setTimeout(()=>{
//                 spinnerBox.classList.add('not-visible')
//                 data.map(post=>{
//                     // console.log(post.id)
//                     postsBox.innerHTML += `
//                         <div class="card p-3 mt-3 mb-3">
//                             ${post.tytul}
//                             <br>
//                             ${post.opis}
//                         </div>
//                     `
//                 })
//             },500)
//             if(max_size){
//                 console.log('done')
//                 loadBox.innerHTML = "<h4>No more posts to load</h4>"
//             }
//         },
//         error: function(error){
//             console.log(error)
//         }
//     })
// }
// handleGetData()

// loadBtn.addEventListener('click', ()=>{
//     visible +=3 
//     handleGetData()
// })