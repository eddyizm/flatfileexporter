
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Resources;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;


namespace FlatFileExporter
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            _mainFrame.Navigate(new MainPage());

        
            //PopulateServerItems();

            //// TODO // may need to pull this from python cli instead or figure out a way to keep them in sync. 
            //// Check version. 
            //var ver = typeof(MainWindow).Assembly.GetName().Version.ToString();
            //MessageBox.Show(ver);
            ///

            //MessageBox.Show("--------------------DEBUGGING-------------------------------");
            //MessageBox.Show(Properties.Settings.Default.IsFirstRun.ToString());
            //SettingsDebugMethod();
            //LoadServers();
            //LoadDataBaseList();

        }

                        
        private static void SettingsDebugMethod()
        {
            // check settings 
            Console.WriteLine("--------------------DEBUGGING-------------------------------");
            MessageBox.Show("--------------------DEBUGGING-------------------------------");
            MessageBox.Show(Properties.Settings.Default.IsFirstRun.ToString());
            Console.WriteLine(Properties.Settings.Default.IsFirstRun.ToString());

            if (Properties.Settings.Default.IsFirstRun == true)
            {
                Properties.Settings.Default.IsFirstRun = false;
                MessageBox.Show("Moving into if statement and changing to false");
                Properties.Settings.Default.Save();
            }
            Console.WriteLine("--------------------DEBUGGING-------------------------------");

            // will need this code to maintain future settings when upgraded
            //Properties.Settings.Default.Upgrade();
            //Properties.Settings.Default.Reset();
            //Properties.Settings.Default.Reload();
        }

        private void Menu_Exit_Click(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }

        private void PopupBox_Closed(object sender, RoutedEventArgs e)
        {
            Console.WriteLine("test");
        }

        private void MenuItem_Server_Click(object sender, RoutedEventArgs e)
        {
            _mainFrame.Navigate(new ServerPage());
        }

        private void MenuItem_Credentials_Click(object sender, RoutedEventArgs e)
        {
            _mainFrame.Navigate(new CredentialsPage());
        }

        private void MenuItem_HomeClick(object sender, RoutedEventArgs e)
        {
            _mainFrame.NavigationService.RemoveBackEntry();
            _mainFrame.Content = new MainPage();
        }

        private void MenuItem_Database_Click(object sender, RoutedEventArgs e)
        {
            _mainFrame.Navigate(new DatabasePage());
        }

        private void MenuItemAbout_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                var folder = Environment.CurrentDirectory;
                var ff_cli = System.IO.Path.Combine(folder, "Resources\\flatfile_cli.exe");
                ProcessStartInfo processStartInfo = new ProcessStartInfo(ff_cli, "-V");
                //ProcessStartInfo processStartInfo = new ProcessStartInfo(ff_cli, "--help");
                processStartInfo.RedirectStandardOutput = true;
                processStartInfo.UseShellExecute = false;
                processStartInfo.CreateNoWindow = true;
                Process p = Process.Start(processStartInfo);
                string output = p.StandardOutput.ReadToEnd();
                p.WaitForExit();
                MessageBox.Show($"{output}", "Beta build");
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error getting verison:{ex.ToString()}");
            }

        }

        

        }
}
