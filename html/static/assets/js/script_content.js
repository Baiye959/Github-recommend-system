// Select all elements with the "i" tag and store them in a NodeList called "stars"
const stars = document.querySelectorAll(".star i");

document.addEventListener("DOMContentLoaded", function() {
    const starsContainer = document.querySelector(".star");
    const myrating = parseInt(starsContainer.dataset.rating);

    stars.forEach((star, index) => {
        // Add the "active" class to the clicked star and any stars with a lower index
        // and remove the "active" class from any stars with a higher index
        myrating > index ? star.classList.add("active") : star.classList.remove("active");
    });
});


// Loop through the "stars" NodeList
stars.forEach((star, index1) => {
  // Add an event listener that runs a function when the "click" event is triggered
  star.addEventListener("click", () => {
    // Loop through the "stars" NodeList Again
    stars.forEach((star, index2) => {
      // Add the "active" class to the clicked star and any stars with a lower index
      // and remove the "active" class from any stars with a higher index
      index1 >= index2 ? star.classList.add("active") : star.classList.remove("active");
    });


    const selectedStars = document.querySelectorAll(".star i.active");
	const selectedCount = selectedStars.length;
    console.log("Selected stars: " + selectedCount);
    data = {
        "githubId": githubId,
        "rating": selectedCount
    }

    $.ajax({
        url: "/content/star",
        type: "POST",
        dataType: "json",
        contentType: 'application/json',
        cache: false,
        async: true,
        data: JSON.stringify(data)
    });

  });
  
});





// Select all elements with the "i" tag and store them in a NodeList called "stars"
const collect_stars = document.querySelectorAll(".collect_star i");

document.addEventListener("DOMContentLoaded", function() {
    const collect_starsContainer = document.querySelector(".collect_star");
    const myrating = parseInt(collect_starsContainer.dataset.rating);

    collect_stars.forEach((star, index) => {
        // Add the "active" class to the clicked star and any stars with a lower index
        // and remove the "active" class from any stars with a higher index
        myrating > index ? collect_star.classList.add("active") : collect_star.classList.remove("active");
    });
});


const collect_star = document.querySelectorAll(".collect_star i")[0];
// Add an event listener that runs a function when the "click" event is triggered
collect_star.addEventListener("click", () => {
    const collect_selectedStars = document.querySelectorAll(".collect_star i.active");
    is_collect = collect_selectedStars.length;
    is_collect == 0 ? collect_star.classList.add("active") : collect_star.classList.remove("active");
    
    
    data = {
        "is_collect": 1-is_collect,
        "githubId": githubId
    }

    $.ajax({
        url: "/content/collect",
        type: "POST",
        dataType: "json",
        contentType: 'application/json',
        cache: false,
        async: true,
        data: JSON.stringify(data)
    });

});
