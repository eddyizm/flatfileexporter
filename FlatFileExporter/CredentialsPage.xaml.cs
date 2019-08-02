using System;
using System.Collections.Generic;
using System.Linq;
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
using System.Windows.Shapes;

namespace FlatFileExporter
{
    /// <summary>
    /// Interaction logic for Credentials.xaml
    /// </summary>
    public partial class CredentialsPage : Page
    {
        public CredentialsPage()
        {
            InitializeComponent();
            LoadCredentials();
        }

        private void LoadCredentials()
        {
            try
            {
                if (!string.IsNullOrEmpty(Properties.Settings.Default.Username))
                {
                    txUserName.Text = Properties.Settings.Default.Username;
                }
                if (!string.IsNullOrEmpty(Properties.Settings.Default.Password))
                {
                    txPassword.Password = Properties.Settings.Default.Password;
                }
            }
            catch (Exception ex)
            {
                throw;
            }
            
        }

        private void ExUserPass_Expanded(object sender, RoutedEventArgs e)
        {
            exTrustConnnect.IsExpanded = false;
        }

        private void btnClear_Click(object sender, RoutedEventArgs e)
        {
            MainWindow mw = Application.Current.Windows.OfType<MainWindow>().FirstOrDefault();
            if (mw != null)
            {
                mw._mainFrame.NavigationService.RemoveBackEntry();
                mw._mainFrame.Content = new MainPage();
            }
        }

        private void btnSaveCred_Click(object sender, RoutedEventArgs e)
        {

            if (!AreCredentialsValid())
                return;
            try
            {
                Properties.Settings.Default.Username = txUserName.Text;
                Properties.Settings.Default.Password = txPassword.Password.ToString();
                Properties.Settings.Default.Save();
                MessageBox.Show("Credentials successfully saved.");
            }
            catch (NullReferenceException ex)
            {
                MessageBox.Show(ex.ToString());
            }
        }

        private bool AreCredentialsValid()
        {
            if (string.IsNullOrEmpty(txUserName.Text) || string.IsNullOrEmpty(txPassword.Password.ToString())) 
            {
                MessageBox.Show("Please enter a username and password.");
                return false;
            }
            return true;
            
        }
    }
}
