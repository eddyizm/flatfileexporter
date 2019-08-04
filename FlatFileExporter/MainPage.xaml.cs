using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Win32;
using System.Windows;
using System.Windows.Controls;
using System.Diagnostics;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Collections.ObjectModel;
using System.IO;

namespace FlatFileExporter
{
    /// <summary>
    /// Interaction logic for MainPage.xaml
    /// </summary>
    public partial class MainPage : Page
    {


        public MainPage()
        {
            InitializeComponent();
            PopulateServerItems();
            LoadDataBaseList();
        }


        #region button clicks 

        private void BtnOpenFile_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                OpenFileDialog openFileDialog = new OpenFileDialog();
                openFileDialog.InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
                openFileDialog.Filter = "SQL files (*.sql)|*.sql|All files (*.*)|*.*"; ;
                openFileDialog.ShowDialog();
                if (!string.IsNullOrEmpty(openFileDialog.FileName))
                {
                    tSqlScript.Text = openFileDialog.FileName;
                }
            }
            catch (Exception ex)
            {

                MessageBox.Show($"Error getting file. Tech Details:{ex.ToString()}");
            }

        }

        private void BtnGenerateFile_Click(object sender, RoutedEventArgs e)
        {
            if (!ValidateFields())
            {
                MessageBox.Show("Please make sure you select a Sql Script, Server, Database and Delimiter.");
                return;
            }
            // this needs to be wrapped into a seperate function and possibly class.
            var checkedExtension = stkExtensionGroup.Children.OfType<RadioButton>()
                                      .FirstOrDefault(r => r.IsChecked == true).Content.ToString();
            CallCommandLine(tSqlScript.Text, cbServers.Text, cbDataBase.Text, checkedExtension, cbDelimiter.Text);
        }

        
        private void CallCommandLine(string sqlscript, string svr, string db, string ext, string delim)
        {

            try
            {
                var folder = Environment.CurrentDirectory;
                var ff_cli = System.IO.Path.Combine(folder, "Resources\\flatfile_cli.exe");
                // command = f'{FILE_EXPORT} PRODSTAR01 HPDataRaw {EXPORT_PATH} {healthplan} .xlsx "|" -sp "EXEC usp_GenerateMMR_UniversalFile \'{healthplan}\',\'{filename}\'" '
                // TODO - construct command
                var myDocs = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
                //var command = $"\"{ff_cli}\" {svr} {db} \"{myDocs}\"";
                var args = $"{svr} {db} \"{myDocs}\" {ext}";
                
                ProcessStartInfo processStartInfo = new ProcessStartInfo(ff_cli);
                // added properties to funnel output to a text and avoid the shell
                processStartInfo.RedirectStandardOutput = true;
                processStartInfo.UseShellExecute = false;
                processStartInfo.CreateNoWindow = true;
                processStartInfo.Arguments = args;
                Process p = Process.Start(processStartInfo);
                string output = p.StandardOutput.ReadToEnd();
                Console.WriteLine(output);
                p.WaitForExit();
                MessageBox.Show($"Log!:\n'{output}'");



            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error calling CLI. Details:{ex.ToString()}");
                
            }
   
            
        }

        private void btnAddServer_Click(object sender, RoutedEventArgs e)
        {
            MainWindow mw = Application.Current.Windows.OfType<MainWindow>().FirstOrDefault();
            if (mw != null)
                mw._mainFrame.NavigationService.RemoveBackEntry();
                mw._mainFrame.Content = new ServerPage();
            
        }

        private void btnAddDatabase_Click(object sender, RoutedEventArgs e)
        {
            MainWindow mw = Application.Current.Windows.OfType<MainWindow>().FirstOrDefault();
            if (mw != null)
                mw._mainFrame.NavigationService.RemoveBackEntry();
            mw._mainFrame.Content = new DatabasePage();
        }

        private void BtnClear_Click(object sender, RoutedEventArgs e)
        {
            MainWindow mw = Application.Current.Windows.OfType<MainWindow>().FirstOrDefault();
            if (mw != null)
            {
                mw._mainFrame.NavigationService.RemoveBackEntry();
                mw._mainFrame.Content = new MainPage();
            }

        }
        #endregion

        #region form validations
        private bool ValidateFields()
        {
            var result = string.IsNullOrEmpty(tSqlScript.Text);

            if (result)
            {
                return false;
            }

            if (cbServers.SelectedIndex == -1)
            {
                return false;
            }
            
            if (cbDataBase.SelectedIndex == -1)
            {
                
                return false;
            }
            
            if (cbDelimiter.SelectedIndex == -1)
            {
                return false;
            }

            return true;
        }
        #endregion

        #region load data
        /// <summary>
        /// Populates server list from user settings
        /// </summary>
        private void PopulateServerItems()
        {

            cbServers.Items.Clear();
            var sCount = Properties.Settings.Default.Servers.Count;
            if (sCount > 0)
            {
                string[] serverList = new string[sCount];
                Properties.Settings.Default.Servers.CopyTo(serverList, 0);
                foreach (var x in serverList)
                {
                    var cbServerItem = new ComboBoxItem { Content = x };
                    cbServers.Items.Add(cbServerItem);
                }
            }
            
        }

        /// <summary>
        /// Populates database list from user settings
        /// </summary>
        private void LoadDataBaseList()
        {
            var dbCount = Properties.Settings.Default.Databases.Count;
            if (dbCount > 0)
            {
                string[] dbList = new string[dbCount];
                Properties.Settings.Default.Databases.CopyTo(dbList, 0);
                foreach (var x in dbList)
                {
                    var cbDatabaseItem = new ComboBoxItem { Content = x };
                    cbDataBase.Items.Add(cbDatabaseItem);
                }
            }
        }

        #endregion

        
    }
}
