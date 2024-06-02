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
    chrome.storage.local.set({ "selectedText": selectedText }, () => {
      chrome.action.setPopup({ tabId: tab.id, popup: 'popup.html' });
      chrome.action.openPopup();
    });
  }
});
