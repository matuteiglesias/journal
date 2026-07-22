document.addEventListener("nav", () => {
  for (const input of document.querySelectorAll<HTMLInputElement>(".page-list-filter")) {
    const list = input.parentElement?.querySelector(".section-ul")
    if (!list) continue

    const update = () => {
      const query = input.value.trim().toLocaleLowerCase()
      for (const item of list.querySelectorAll<HTMLLIElement>(".section-li")) {
        item.hidden = query !== "" && !item.textContent?.toLocaleLowerCase().includes(query)
      }
    }

    input.addEventListener("input", update)
    window.addCleanup(() => input.removeEventListener("input", update))
  }
})
