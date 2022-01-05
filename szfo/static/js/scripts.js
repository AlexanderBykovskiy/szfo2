// Click on mobil menu button
const mobilMenuClickHandler = () => {
	const mobilMenuContainer = document.getElementById('mobil_menu_container')
	mobilMenuContainer.classList.remove('hide')
}

const hideMobilMenuClickHandler = () => {
	const mobilMenuContainer = document.getElementById('mobil_menu_container')
	mobilMenuContainer.classList.add('hide')
}