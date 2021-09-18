const navigateTo = url => {
    history.pushState(null, null, url);
    router();
};
const router = async () => {
  const routes = [
    {path: "/", view: ()=> console.log('route /')},
    {path: "/cards", view: ()=> console.log('route /cards')},
    {path: "/yourcard", view: ()=> console.log('route /yourcard')},
    {path: "/about", view: ()=> console.log('route /about')}
  ]  
    
const matches = routes.map(route => {
    return {
        route: route,
        isMatch: location.pathname === route.path
    }
})
    let match = matches.find(matches => matches.isMatch)
   console.log(match.route.view()) 

    
};
window.addEventListener("popstate", router);
document.addEventListener("DOMContentLoaded", ()=>{
    document.body.addEventListener("click", e => {
        if (e.target.matches("[data-link]")) {
            e.preventDefault();
            navigateTo(e.target.href);
        }
    });
    router();})
