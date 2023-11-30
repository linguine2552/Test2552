--
-- Database: 'lorem_ipsum_jobportal'
--
-- --------------------------------------------------------
-- Table structure for table 'Work_Request'
DROP TABLE IF EXISTS 'Work_Request';
CREATE TABLE IF NOT EXISTS 'Work_Request' (
  Request_id INT AUTO_INCREMENT PRIMARY KEY,
  'WR_Fname' varchar(225) NOT NULL,
  'WR_Lname' varchar(225) NOT NULL,
  'WR_Email' varchar(225) NOT NULL,
  'WR_Phone' varchar(20) NOT NULL,
  'WR_Company' varchar(225) NOT NULL,
  'WR_website' varchar(225) NOT NULL,
 'JobDiscription' TEXT,
StateCode ENUM('one','two','three','four') NOT NULL,
RegistrationType ENUM('one','two','three','four') NOT NULL
) 

-- --------------------------------------------------------
-- Table structure for table 'User_Account'
DROP TABLE IF EXISTS 'User_Account';
CREATE TABLE IF NOT EXISTS 'User_Account' (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  'fname' varchar(225) NOT NULL,
  'lname' varchar(225) NOT NULL,
  'email' varchar(225) NOT NULL,
  'phone' varchar(20) NOT NULL,
  'company' varchar(225) NOT NULL,
  'website' varchar(225) NOT NULL
) 

-- --------------------------------------------------------
--
-- Table structure for table 'admin'
--

DROP TABLE IF EXISTS 'admin';
CREATE TABLE IF NOT EXISTS 'admin' (
  'admin_id' int(20) NOT NULL,
  'admin_name' varchar(100) NOT NULL,
  'admin_pass' varchar(100) NOT NULL
) 

-- --------------------------------------------------------

--
-- Table structure for table 'application'
--

DROP TABLE IF EXISTS 'application';
CREATE TABLE IF NOT EXISTS 'application' (
  'apply_id' int(20) NOT NULL AUTO_INCREMENT,
  'user_id' int(20) DEFAULT NULL,
  'emp_id' int(20) DEFAULT NULL,
  'job_id' int(20) DEFAULT NULL,
  'status' int(20) DEFAULT NULL,
  'date_applied' varchar(20) NOT NULL,
  PRIMARY KEY ('apply_id'),
  KEY 'user_id' ('user_id'),
  KEY 'emp_id' ('emp_id'),
  KEY 'job_id' ('job_id')
)

-- --------------------------------------------------------

--
-- Table structure for table 'employer'
--

DROP TABLE IF EXISTS 'employer';
CREATE TABLE IF NOT EXISTS 'employer' (
  'employer_id' int(20) NOT NULL AUTO_INCREMENT,
  'log_id' int(20) NOT NULL,
  'employer_name' varchar(100) DEFAULT NULL,
  'address' varchar(200) DEFAULT NULL,
  'pincode' varchar(100) DEFAULT NULL,
  'executive' varchar(100) DEFAULT NULL,
  'phone' varchar(100) DEFAULT NULL,
  'location' varchar(200) DEFAULT NULL,
  'profile' varchar(700) DEFAULT NULL,
  'logo' varchar(50) DEFAULT NULL,
  PRIMARY KEY ('employer_id'),
  KEY 'log_id' ('log_id')
)

-- --------------------------------------------------------

--
-- Table structure for table 'jobs'
--

DROP TABLE IF EXISTS 'jobs';
CREATE TABLE IF NOT EXISTS 'jobs' (
  'jobid' int(20) NOT NULL AUTO_INCREMENT,
  'employer_id' int(20) NOT NULL,
  'title' varchar(100) DEFAULT NULL,
  'jobdesc' varchar(700) NOT NULL,
  'job_opening_number' int(20) DEFAULT NULL,
  'experience' varchar(100) DEFAULT NULL,
  'basicpay' varchar(100) DEFAULT NULL,
  'fnarea' varchar(100) DEFAULT NULL,
  'location' varchar(200) DEFAULT NULL,
  'ugqual' varchar(100) DEFAULT NULL,
  'pgqual' varchar(100) DEFAULT NULL,
  'profile' varchar(700) DEFAULT NULL,
  'postdate' varchar(20) NOT NULL,
  PRIMARY KEY ('jobid'),
  KEY 'employer_id' ('employer_id')
)

-- --------------------------------------------------------

--
-- Table structure for table 'jobseeker'
--

DROP TABLE IF EXISTS 'jobseeker';
CREATE TABLE IF NOT EXISTS 'jobseeker' (
  'user_id' int(20) NOT NULL AUTO_INCREMENT,
  'log_id' int(20) DEFAULT NULL,
  'name' varchar(100) NOT NULL,
  'email' varchar(255) NOT NULL,
  'phone' varchar(20) DEFAULT NULL,
  'country_code' varchar(200) DEFAULT NULL,
  'zip_code' varchar(200) DEFAULT NULL,
  'experience' varchar(100) DEFAULT NULL,
  'skills' varchar(100) DEFAULT NULL,
  'other_qual' varchar(100) DEFAULT NULL,
  'dob' varchar(50) DEFAULT NULL,
  PRIMARY KEY ('user_id'),
  KEY 'log_id' ('log_id')
)

-- --------------------------------------------------------

--
-- Table structure for table 'login'
--

DROP TABLE IF EXISTS 'login';
CREATE TABLE IF NOT EXISTS 'login' (
  'log_id' int(20) NOT NULL AUTO_INCREMENT,
  'email' varchar(100) DEFAULT NULL,
  'password' varchar(250) DEFAULT NULL,
  'usertype' varchar(20) NOT NULL,
  'status' int(1) DEFAULT NULL,
  PRIMARY KEY ('log_id'),
  UNIQUE KEY 'email' ('email'),
  KEY 'log_id' ('log_id'),
  KEY 'log_id_2' ('log_id')
)

-- --------------------------------------------------------

--
-- Table structure for table 'selection'
--

DROP TABLE IF EXISTS 'selection';
CREATE TABLE IF NOT EXISTS 'selection' (
  'sel_id' int(20) NOT NULL AUTO_INCREMENT,
  'user_id' int(20) DEFAULT NULL,
  'emp_id' int(20) DEFAULT NULL,
  'job_id' int(20) DEFAULT NULL,
  'status' int(5) DEFAULT NULL,
  'date' varchar(20) NOT NULL,
  PRIMARY KEY ('sel_id'),
  KEY 'user_id' ('user_id'),
  KEY 'emp_id' ('emp_id'),
  KEY 'job_id' ('job_id')
)

--
-- Constraints for dumped tables
--

--
-- Constraints for table 'application'
--
ALTER TABLE 'application'
  ADD CONSTRAINT 'fk_empid' FOREIGN KEY ('emp_id') REFERENCES 'employer' ('employer_id') ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT 'fk_job' FOREIGN KEY ('job_id') REFERENCES 'jobs' ('jobid') ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT 'fk_userid' FOREIGN KEY ('user_id') REFERENCES 'jobseeker' ('user_id') ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table 'employer'
--
ALTER TABLE 'employer'
  ADD CONSTRAINT 'fk_log_id' FOREIGN KEY ('log_id') REFERENCES 'login' ('log_id') ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table 'jobs'
--
ALTER TABLE 'jobs'
  ADD CONSTRAINT 'fk_employer_id' FOREIGN KEY ('employer_id') REFERENCES 'employer' ('employer_id') ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table 'jobseeker'
--
ALTER TABLE 'jobseeker'
  ADD CONSTRAINT 'fk_login' FOREIGN KEY ('log_id') REFERENCES 'login' ('log_id') ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table 'selection'
--
ALTER TABLE 'selection'
  ADD CONSTRAINT 'fk_emp' FOREIGN KEY ('emp_id') REFERENCES 'employer' ('employer_id') ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT 'fk_jobs' FOREIGN KEY ('job_id') REFERENCES 'jobs' ('jobid') ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT 'fk_user' FOREIGN KEY ('user_id') REFERENCES 'jobseeker' ('user_id') ON DELETE CASCADE ON UPDATE CASCADE;
