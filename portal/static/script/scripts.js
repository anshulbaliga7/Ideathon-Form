function myfunc() 
{
  var checkbox = document.getElementById("mycheck");
  if (checkbox.checked == true) return true;
  else return false;
}

function submitfunction() 
{
  var formyy = document.getElementById("ideathon-form");
  const fbde = document.querySelector('input[name="businessidea"]');

  if (fbde.value != "") 
  {
    if (myfunc() == true) 
    {
      var res = confirm("Are you sure you want to submit?");
      if (res == false) 
      {
        return false;
      } else if (res == true) 
      {
        formyy.submit();
        alert("Successfully Submitted!");
      }
    } 
    else 
    {
      alert("Please check the tickbox");
    }
  } 
  else 
  {
    alert("Please fill out all the fields");
  }
}

function clearfunction() 
{
  var ch = document.getElementById("ideathon-form");
  var ch2 = document.getElementById("mycheck");
  if (ch2.checked == true) {
    ch2.checked = false;
  }
  ch.reset();
}

function clicky() {
  document.getElementById("personalinfo-section").style.display = "none";
}
function clicky1() {
  document.getElementById("personalinfo-section").style.display = "block";
}
function clicky2() {
  document.getElementById("aboutidea-section").style.display = "none";
}
function clicky3() {
  document.getElementById("aboutidea-section").style.display = "block";
}
function clicky4() {
  document.getElementById("team-details-section").style.display = "none";
}
function clicky5() {
  document.getElementById("team-details-section").style.display = "block";
}

function displaymodal() {
  const project_id_input = document.getElementById("project_id_input");
  const modal_project_id_input = document.getElementById("modal_project_id_input");

  const project_id = project_id_input.value;
  modal_project_id_input.value = project_id;
  var modal1 = document.getElementById("member-details-modal");
  modal1.style.display = "block";
  window.onclick = function (event) {
    if (event.target == modal1) {
      modal1.style.display = "none";
    }
  };
}

function closefunc() {
  var m1 = document.getElementById("member-details-modal");
  m1.style.display = "none";
}

function specifyhidden(i) {
  var m1 = document.getElementById("specifyhide");
  if (i == 10) {
    m1.style.display = "block";
  } else {
    m1.style.display = "none";
  }
}

let memberCount = 0;

function submitmemberdetails() {
  memberCount++;
  const number = memberCount;
  const projectId = document.getElementById("main_form_id_input").value; // Get the project ID from the main form
  const name = document.querySelector('input[name="memnameone"]').value;
  const contactNumber = document.querySelector('input[name="memcontone"]').value;
  const email = document.querySelector('input[name="memmailone"]').value;
  const dob = document.querySelector('input[name="memdobone"]').value;
  const gender = document.querySelector('select[name="memgenone"]').value;
  const tsipDepartment = document.querySelector('input[name="memdeptone"]').value;
  const role = document.querySelector('input[name="memroleone"]').value;
  const coreCompetency = document.querySelector('input[name="memcoreone"]').value;
  if (name !== "" && coreCompetency !== "") 
  {
    const table = document.getElementById("member-table");
    const row = table.insertRow();

    const cells = [
      number,
      name,
      contactNumber,
      email,
      dob,
      gender,
      tsipDepartment,
      role,
      coreCompetency,
    ];
    cells.forEach((value, index) => {
      const cell = row.insertCell(index);
      cell.textContent = value;
    });
    table.style.display="block";

    const formData = new FormData();
    formData.append("id", projectId);
    formData.append("memnameone", name);
    formData.append("memcontone", contactNumber);
    formData.append("memmailone", email);
    formData.append("memdobone", dob);
    formData.append("memgenone", gender);
    formData.append("memdeptone", tsipDepartment);
    formData.append("memroleone", role);
    formData.append("memcoreone", coreCompetency);

    const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

    fetch("/save-member-details/", {
      method: "POST",
      headers: {
        "X-CSRFToken": csrftoken,
      },
      body: formData,
    })
      .then((response) => response.text())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.error(error);
      });


    document.querySelector('input[name="memnameone"]').value = "";
    document.querySelector('input[name="memcontone"]').value = "";
    document.querySelector('input[name="memmailone"]').value = "";
    document.querySelector('input[name="memdobone"]').value = "";
    document.querySelector('select[name="memgenone"]').value = "M";
    document.querySelector('input[name="memdeptone"]').value = "";
    document.querySelector('input[name="memroleone"]').value = "";
    document.querySelector('input[name="memcoreone"]').value = "";
  } 
  else 
  {
    alert("Fill in all the details.");
  }
}


function validateContacts(event) {
  const input = event.target;
  const inputValue = input.value;
  
  const digitsOnly = inputValue.replace(/\D/g, '');
  
  const limitedValue = digitsOnly.slice(0, 10);
  
  input.value = limitedValue;
}

function uploadDocument() {
  // Get the selected file from the input element
  const fileInput = document.getElementById('document-upload');
  const file = fileInput.files[0];

  // Create a FormData object to send the file to the backend
  const formData = new FormData();
  formData.append('document', file);

  // Send the file to the backend using AJAX
  const xhr = new XMLHttpRequest();
  xhr.open('POST', 'upload-document/', true);
  xhr.onload = function () {
    if (xhr.status === 200) {
      // Document uploaded successfully
      alert('Document uploaded successfully!');
    } else {
      // Error occurred during upload
      alert('Error uploading document.');
    }
  };
  xhr.send(formData);
}



