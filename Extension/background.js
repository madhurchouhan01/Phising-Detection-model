chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "checkPhishing",
    title: "Check if Phishing",
    contexts: ["selection"]
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "checkPhishing") {
    const selectedText = info.selectionText;
    console.log(selectedText);

    // Store the selected text in local storage
    chrome.storage.local.set({ "selectedText": selectedText }, () => {
      // Open the popup window
      chrome.browserAction.openPopup();
    });
  }
});
